from datetime import datetime, timedelta

from django.core.paginator import Paginator
from django.db.models import OuterRef, Q, Subquery
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.models import Inventory, OrderRequest, Warehouse
from api.models.common import Status
from api.models.warehouse import WarehouseTransaction, WhTomasFisicas
from api.serializers.order import OrderSerializer
from api.serializers.warehouse import (
    FullWarehouseSerializer,
    TomasFisicasSerializer,
    WarehouseSerializer,
    WhInventorySerializer,
    WhTransactionSerializer,
    WhWithTomaFisicaSerializer,
)
from api.utils import error_response


class WarehouseView(APIView):
    """
    This View holds multiple methods for the Warehouse
    """

    def get(self, request: Request):

        try:

            querydict = request.query_params

            filters = {}

            for key, value in querydict.items():
                if key in ["id", "name", "latitude", "longitude"]:
                    filters[key] = value

            warehouse_qset = Warehouse.objects.filter(**filters)

            warehouse_qset = warehouse_qset.exclude(status__name="invalid").latest("id")

            serializer = WarehouseSerializer(warehouse_qset)

            return JsonResponse(serializer.data)

        except Exception as e:
            error_response("Invalid query")

    def put(self, request: Request):

        try:

            queryid = request.query_params.get("id")

            data = dict(**request.data)

            warehouse = Warehouse.objects.get(id=queryid)

            serializer = WarehouseSerializer(warehouse, data=data)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            return JsonResponse({"error": False, "message": serializer.data})

        except Exception as e:
            error_response("Invalid query")

    def post(self, request: Request):

        data = dict(**request.data)

        try:

            valid_status = Status.objects.get(name="active")

            data["status"] = valid_status.id

            serializer = WarehouseSerializer(data=data)

            serializer.is_valid(raise_exception=True)

            serializer.update()

        except Exception as e:
            error_response("Invalid query")

        return JsonResponse({"error": False, "message": "Ok"})

    def delete(self, request: Request):
        """
        This method would deactivate a warehouse.
        Args:
            request: The Request

        Returns:
            A response with the status information about the action
            executed.

        """
        try:
            querydict = request.query_params

            filters = {}

            for key, value in querydict.items():
                if key in ["id", "name", "latitude", "longitude"]:
                    filters[key] = value

            filters["status"] = Status.objects.get(name="active")

            inactive_status = Status.objects.get(name="inactive")

            updateted_rows = Warehouse.objects.filter(**filters).update(
                status=inactive_status
            )

            return JsonResponse(
                {"error": False, "message": "Rows affected: " + str(updateted_rows)},
            )

        except Exception as e:

            error_response("Invalid query")


class WarehouseViewSet(ReadOnlyModelViewSet):

    queryset = Warehouse.objects.all().order_by("name").exclude(status__name="inactive")
    serializer_class = FullWarehouseSerializer


class FullWarehouseViewSet(WarehouseViewSet):
    pagination_class = None


class OrderRequestViewSet(ReadOnlyModelViewSet):
    queryset = OrderRequest.objects.all().order_by("id")
    serializer_class = OrderSerializer(queryset, many=True)

    def list(self, request):

        page_number = request.query_params.get("page")

        if page_number:

            paginator = Paginator(self.queryset, 50)

            page_obj = paginator.get_page(page_number)

            return Response(OrderSerializer(page_obj, many=True).data)

        return Response(self.serializer_class.data)


class WhInventorysViewSet(ModelViewSet):

    queryset = Inventory.objects.all().order_by("-id")
    serializer_class = WhInventorySerializer

    def get_queryset(self):
        queryset = self.queryset
        params = self.request.query_params.copy()

        if params.get("order_by", None):
            fields = params.pop("order_by")
            queryset = queryset.order_by(*fields)

        if params.get("id", None):
            queryset = queryset.filter(id=params.get("id", None))
            return queryset

        if params.get("warehouse_id", None):
            queryset = queryset.filter(
                warehouse_id=params.get("warehouse_id")
            ).prefetch_related("item")

        if params.get("name", None):
            queryset = queryset.filter(item__name__icontains=params.get("name"))

        if params.get("codename", None):
            queryset = queryset.filter(item__codename__icontains=params.get("codename"))

        if params.get("min_quantity", None):
            queryset = queryset.filter(quantity__gte=params.get("min_quantity"))

        if params.get("max_quantity", None):
            queryset = queryset.filter(quantity__lte=params.get("max_quantity"))

        if params.get("min_price", None):
            queryset = queryset.filter(item__price__gte=params.get("min_price"))

        if params.get("max_price", None):
            queryset = queryset.filter(item__price__lte=params.get("max_price"))

        if params.get("from_date", None):
            queryset = queryset.filter(updated_at__gte=(params["from_date"]))
        #%H:%M:%S
        if params.get("to_date", None):
            to_date = datetime.strptime(
                (params.get("to_date")), "%Y-%m-%dT%H:%M:%S.%f%z"
            ) + timedelta(days=1)

            queryset = queryset.filter(updated_at__lte=to_date)

        return queryset


class WhOrderRequestView(APIView):
    def get(self, request):

        try:

            wh_orders = OrderRequest.objects.filter(
                warehouse__pk=request.query_params.get("id")
            ).order_by("-id")

            page_number = request.query_params.get("page")

            if page_number:

                paginator = Paginator(
                    wh_orders, request.query_params.get("per_page", 15)
                )

                page_obj = paginator.get_page(page_number)

                return JsonResponse(
                    {
                        "data": OrderSerializer(page_obj, many=True).data,
                        "total": paginator.count,
                        "page": int(page_number),
                        "lastPage": paginator.num_pages,
                    }
                )

            return Response(OrderSerializer(wh_orders, many=True).data)

        except:
            return error_response("Invalid query")


class WhTransactionViewSet(ModelViewSet):

    queryset = WarehouseTransaction.objects.all().order_by("-created_at")
    serializer_class = WhTransactionSerializer

    def get_queryset(self):
        queryset = self.queryset.select_related("created_by", "status")
        params = self.request.query_params.copy()

        if params.get("order_by", None):
            fields = params.pop("order_by")
            queryset = queryset.order_by(*fields)

        if params.get("id", None):
            queryset = queryset.filter(id=params.get("id"))
            return queryset

        if params.get("warehouse_id", None):

            if params.get("entrada", None) and params.get("salida", None):
                queryset = queryset.filter(
                    Q(warehouse_destiny=params.get("warehouse_id"))
                    | Q(warehouse_origin=params.get("warehouse_id"))
                )
            elif params.get("entrada", None):
                queryset = queryset.filter(warehouse_destiny=params.get("warehouse_id"))
            elif params.get("salida", None):
                queryset = queryset.filter(warehouse_origin=params.get("warehouse_id"))

        if params.get("warehouse_name", None):

            if params.get("entrada", None) and params.get("salida", None):
                queryset = queryset.filter(
                    Q(warehouse_destiny__name__icontains=params.get("warehouse_name"))
                    | Q(warehouse_origin__name__icontains=params.get("warehouse_name"))
                )

            elif params.get("entrada", None):
                queryset = queryset.filter(
                    warehouse_destiny__name__icontains=params.get("warehouse_name")
                )

            elif params.get("salida", None):
                queryset = queryset.filter(
                    warehouse_origin__name__icontains=params.get("warehouse_name")
                )

        if params.get("from_date", None):
            queryset = queryset.filter(created_at__gte=(params.get("from_date")))

        if params.get("to_date", None):
            to_date = datetime.strptime(
                (params.get("to_date")), "%Y-%m-%dT%H:%M:%S.%f%z"
            ) + timedelta(days=1)
            queryset = queryset.filter(created_at__lte=to_date)

        if params.get("notes", None):
            queryset = queryset.filter(notes__icontains=(params.get("from_date")))

        if params.get("created_by", None):
            queryset = queryset.filter(created_by=(params.get("created_by")))

        if params.get("created_by_name", None):
            queryset = queryset.filter(
                created_by__name__icontains=(params.get("created_by_name"))
            )
            queryset = queryset.filter(
                created_by__lastname__icontains=(params.get("created_by_name"))
            )

        return queryset


class WhOrderRequestViewSet(ReadOnlyModelViewSet):
    """
    API Endpoint that allows only read operation on the given Orders that are registered and available
    """

    queryset = OrderRequest.objects.all().order_by("id")
    serializer_class = OrderSerializer(queryset, many=True)


class WhLatestTomaFisicaView(APIView):
    def get(self, request):
        try:

            latest_tf = WhTomasFisicas.objects.filter(
                warehouse=OuterRef("id")
            ).order_by("-id")[:1]

            wh_with_toma_fisica = Warehouse.objects.annotate(
                whtf_id=Subquery(latest_tf.values("id")),
                whtf_created_at=Subquery(latest_tf.values("created_at")),
                whtf_novedad=Subquery(latest_tf.values("novedad")),
                whtf_done_by_name=Subquery(latest_tf.values("done_by__name")),
                whtf_done_by_lastname=Subquery(latest_tf.values("done_by__lastname")),
            ).order_by("name")

            serializer = WhWithTomaFisicaSerializer(wh_with_toma_fisica, many=True)

            return Response(serializer.data)

        except Exception as e:
            return error_response("Invalid query")


class WhTomasFisicasViewSet(ModelViewSet):

    queryset = WhTomasFisicas.objects.all().order_by("-created_at")
    serializer_class = TomasFisicasSerializer

    def get_queryset(self):
        queryset = self.queryset
        params = self.request.query_params.copy()

        if params.get("order_by", None):
            fields = params.pop("order_by")
            queryset = queryset.order_by(*fields)

        if params.get("warehouse_id", None):
            queryset = queryset.filter(
                warehouse=params.get("warehouse_id")
            ).select_related("warehouse", "done_by")

        if params.get("employee_name", None):
            queryset = queryset.filter(
                done_by__name__icontains=params.get("employee_name")
            )

        if params.get("employee_id", None):
            queryset = queryset.filter(done_by__id=params.get("employee_id"))

        if params.get("novedad", None):
            queryset = queryset.filter(novedad__icontains=params.get("novedad"))

        if params.get("from_date", None):
            queryset = queryset.filter(created_at__gte=(params["from_date"]))

        if params.get("to_date", None):
            to_date = datetime.strptime(
                (params.get("to_date")), "%Y-%m-%dT%H:%M:%S.%f%z"
            ) + timedelta(days=1)
            queryset = queryset.filter(created_at__lte=to_date)

        return queryset
