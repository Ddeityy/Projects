# Generated by Django 4.0.4 on 2022-05-07 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0004_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storefront.material')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storefront.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.ManyToManyField(through='storefront.ProductMaterial', to='storefront.material'),
        ),
    ]
