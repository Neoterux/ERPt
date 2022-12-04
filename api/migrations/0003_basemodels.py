# Generated by Django 4.0.6 on 2022-08-24 00:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_basedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchOfficeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'branch_offices',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=60)),
                ('short_name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='CategoryParamsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('default_value', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=50)),
                ('field_type', models.CharField(max_length=20)),
                ('required', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.categorymodel')),
            ],
            options={
                'db_table': 'category_params',
            },
        ),
        migrations.CreateModel(
            name='CitiesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('address', models.CharField(max_length=256)),
                ('business_name', models.CharField(max_length=128, null=True)),
                ('email', models.EmailField(max_length=32)),
                ('number_id', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=16)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.citiesmodel')),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='CreditNote',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('iva', models.DecimalField(decimal_places=3, max_digits=6)),
                ('return_deadline', models.DateField()),
                ('subtotal', models.DecimalField(decimal_places=3, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('total', models.DecimalField(decimal_places=3, max_digits=14)),
                ('branch_office_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.branchofficemodel')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.clientmodel')),
            ],
            options={
                'db_table': 'credit_note',
            },
        ),
        migrations.CreateModel(
            name='GenderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('short_name', models.CharField(max_length=6, null=True)),
            ],
            options={
                'db_table': 'genders',
            },
        ),
        migrations.CreateModel(
            name='InvoiceDetailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=3, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'db_table': 'invoice_details',
            },
        ),
        migrations.CreateModel(
            name='ItemsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('brand', models.CharField(max_length=128)),
                ('img', models.CharField(max_length=255)),
                ('iva', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('model', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=3, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.categorymodel')),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='OrderRequestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'order_request',
            },
        ),
        migrations.CreateModel(
            name='OrderStatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'order_status',
            },
        ),
        migrations.CreateModel(
            name='ProviderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('name', models.CharField(max_length=128)),
                ('document_path', models.CharField(max_length=128)),
                ('bussiness_name', models.CharField(max_length=128)),
                ('phone_no', models.CharField(max_length=25)),
                ('website', models.URLField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=64)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'provider',
            },
        ),
        migrations.CreateModel(
            name='ProvinceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'provinces',
            },
        ),
        migrations.CreateModel(
            name='PurchaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('reference', models.IntegerField()),
                ('img_details', models.CharField(max_length=255, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.invoicedetailsmodel')),
                ('order_origin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.orderstatusmodel')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.providermodel')),
            ],
            options={
                'db_table': 'purchase',
            },
        ),
        migrations.CreateModel(
            name='StatusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='WharehouseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('name', models.CharField(max_length=128)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel')),
            ],
            options={
                'db_table': 'wharehouse',
            },
        ),
        migrations.CreateModel(
            name='WharehouseTransactionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('notes', models.CharField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'wharehouse_transaction',
            },
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_active',
        ),
        migrations.AddField(
            model_name='employee',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='WhTransactionDetailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.wharehousetransactionmodel')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.itemsmodel')),
            ],
            options={
                'db_table': 'wh_transaction_details',
            },
        ),
        migrations.AddField(
            model_name='wharehousetransactionmodel',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.employee'),
        ),
        migrations.AddField(
            model_name='wharehousetransactionmodel',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel'),
        ),
        migrations.AddField(
            model_name='wharehousetransactionmodel',
            name='wharehouse_destiny',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='destiny', to='api.wharehousemodel'),
        ),
        migrations.AddField(
            model_name='wharehousetransactionmodel',
            name='wharehouse_origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='origin', to='api.wharehousemodel'),
        ),
        migrations.AddField(
            model_name='statusmodel',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.employee'),
        ),
        migrations.CreateModel(
            name='PurchaseStatusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.employee')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.purchasemodel')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel')),
            ],
            options={
                'db_table': 'purchase_status',
            },
        ),
        migrations.AddField(
            model_name='purchasemodel',
            name='wharehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.wharehousemodel'),
        ),
        migrations.CreateModel(
            name='PurchaseDetailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=3, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.itemsmodel')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.purchasemodel')),
            ],
            options={
                'db_table': 'purchase_details',
            },
        ),
        migrations.AddField(
            model_name='providermodel',
            name='created_by',
            field=models.ForeignKey(db_column='created_by', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='creator', to='api.employee'),
        ),
        migrations.AddField(
            model_name='providermodel',
            name='deleted_by',
            field=models.ForeignKey(db_column='deleted_by', default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='remover', to='api.employee'),
        ),
        migrations.AddField(
            model_name='providermodel',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel'),
        ),
        migrations.AddField(
            model_name='providermodel',
            name='updated_by',
            field=models.ForeignKey(db_column='updated_by', default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='updater', to='api.employee'),
        ),
        migrations.CreateModel(
            name='PaymentMethodModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel')),
            ],
            options={
                'db_table': 'payment_method',
            },
        ),
        migrations.AddField(
            model_name='orderstatusmodel',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.employee'),
        ),
        migrations.AddField(
            model_name='orderstatusmodel',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.orderrequestmodel'),
        ),
        migrations.AddField(
            model_name='orderstatusmodel',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel'),
        ),
        migrations.AddField(
            model_name='orderrequestmodel',
            name='requested_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.employee'),
        ),
        migrations.AddField(
            model_name='orderrequestmodel',
            name='wharehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.wharehousemodel'),
        ),
        migrations.CreateModel(
            name='OrderRequestDetailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.itemsmodel')),
                ('order_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.orderrequestmodel')),
            ],
            options={
                'db_table': 'order_request_details',
            },
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.employee'),
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel'),
        ),
        migrations.CreateModel(
            name='ItemMetaDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=100)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.itemsmodel')),
                ('param', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.categoryparamsmodel')),
            ],
            options={
                'db_table': 'item_meta_data',
            },
        ),
        migrations.CreateModel(
            name='InvoiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('iva', models.DecimalField(decimal_places=3, max_digits=6)),
                ('return_deadline', models.DateField()),
                ('subtotal', models.DecimalField(decimal_places=3, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('transaction_code', models.CharField(max_length=128, null=True)),
                ('total', models.DecimalField(decimal_places=3, max_digits=15)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.clientmodel')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.employee')),
                ('credit_note_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.creditnote')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.paymentmethodmodel')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel')),
            ],
            options={
                'db_table': 'invoice',
            },
        ),
        migrations.AddField(
            model_name='invoicedetailsmodel',
            name='invoice_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.invoicemodel'),
        ),
        migrations.AddField(
            model_name='invoicedetailsmodel',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.itemsmodel'),
        ),
        migrations.CreateModel(
            name='InventoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.itemsmodel')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.employee')),
                ('wharehouse', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.wharehousemodel')),
            ],
            options={
                'db_table': 'inventory',
            },
        ),
        migrations.CreateModel(
            name='HistorialCajaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('cantidad_facturas', models.IntegerField()),
                ('fecha_cierre', models.DateTimeField()),
                ('fecha_apertura', models.DateTimeField()),
                ('num_caja', models.IntegerField()),
                ('valor_apertura', models.DecimalField(decimal_places=3, max_digits=10)),
                ('valor_cierre', models.DecimalField(decimal_places=3, max_digits=10)),
                ('1_centavo', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('5_centavo', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('10_centavo', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('25_centavo', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('50_centavo', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('1_dolar_moneda', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('1_dolar_billete', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('5_billete', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('10_billete', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('20_billete', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('50_billete', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('dinero_fisico', models.DecimalField(decimal_places=3, max_digits=13, validators=[django.core.validators.MinValueValidator(0)])),
                ('dinero_faltante', models.DecimalField(decimal_places=3, max_digits=13)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.employee')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel')),
            ],
            options={
                'db_table': 'historial_caja',
            },
        ),
        migrations.AddField(
            model_name='creditnote',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.employee'),
        ),
        migrations.AddField(
            model_name='creditnote',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.paymentmethodmodel'),
        ),
        migrations.AddField(
            model_name='creditnote',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel'),
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.employee'),
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.gendermodel'),
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.provincemodel'),
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel'),
        ),
        migrations.AddField(
            model_name='citiesmodel',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.provincemodel'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel'),
        ),
        migrations.AddField(
            model_name='branchofficemodel',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel'),
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.statusmodel'),
        ),
    ]