import django_tables2 as tables
from .models import Log, Sensor


class LogTableQuerySet(tables.Table):
    sensor_type_column = tables.Column(
        accessor='get_sensor_type', verbose_name='Sensor Type')

    class Meta:
        fields = ['id', 'sensor_code', 'sensor_model', 'sensor_type_column', 'updated_time', 'sensor_status']
        model = Sensor
        template_name = "django_tables2/bootstrap.html"


class MonitoringTableQuerySet(tables.Table):
    sensor_type_column = tables.Column(
        accessor='get_sensor_type', verbose_name='Sensor Type')
    action = tables.TemplateColumn(template_name='tables/action_column.html')

    class Meta:
        fields = ['id', 'sensor_code', 'sensor_model',
                  'sensor_type_column', 'updated_time', 'sensor_status', 'action']
        model = Sensor
        template_name = "django_tables2/bootstrap.html"
