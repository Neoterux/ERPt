# Generated by Django 4.1.2 on 2022-11-14 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_orderrequest_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sequence",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
                ("number", models.IntegerField(null=True)),
            ],
            options={
                "db_table": "sequence",
            },
        ),
        migrations.AddField(
            model_name="invoice",
            name="emission",
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="orderrequest",
            name="approved_at",
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="orderrequest",
            name="approved_by",
            field=models.OneToOneField(
                db_column="approved_by",
                default=None,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="approved_by",
                to="api.employee",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="code",
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="credit_note",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="api.creditnote",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="return_deadline",
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="transaction_code",
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="invoicedetails",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="invoice_details",
                to="api.invoice",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="category",
                to="api.category",
            ),
        ),
        migrations.AlterField(
            model_name="orderrequest",
            name="requested_by",
            field=models.ForeignKey(
                db_column="requested_by",
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="requested_by",
                to="api.employee",
            ),
        ),
        migrations.AlterField(
            model_name="orderrequest",
            name="warehouse",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="warehouse",
                to="api.warehouse",
            ),
        ),
        migrations.AlterField(
            model_name="orderrequestdetail",
            name="order_request",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="api.orderrequest",
            ),
        ),
        migrations.AddIndex(
            model_name="orderrequest",
            index=models.Index(fields=["status"], name="order_reque_status_d5b425_idx"),
        ),
    ]
