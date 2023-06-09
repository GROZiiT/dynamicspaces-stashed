from django.http import HttpResponse
from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'pages-error-404.html', status=404)


def handler500(request):
    return render(request, 'pages-error-404.html', status=500)


def index(request):
    return render(request, "index.html")

def add_post(request):
    return render(request, "add-post.html")

def charts_apexcharts(request):
    return render(request, "charts-apexcharts.html")


def charts_chartjs(request):
    return render(request, "charts-chartjs.html")


def charts_echarts(request):
    return render(request, "charts-echarts.html")


def components_accordion(request):
    return render(request, "components-accordion.html")


def components_alerts(request):
    return render(request, "components-alerts.html")


def components_badges(request):
    return render(request, "components-badges.html")


def components_breadcrumbs(request):
    return render(request, "components-breadcrumbs.html")


def components_buttons(request):
    return render(request, "components-buttons.html")


def components_cards(request):
    return render(request, "components-cards.html")


def components_carousel(request):
    return render(request, "components-carousel.html")


def components_list_group(request):
    return render(request, "components-list-group.html")


def components_modal(request):
    return render(request, "components-modal.html")


def components_pagination(request):
    return render(request, "components-pagination.html")


def components_progress(request):
    return render(request, "components-progress.html")


def components_spinners(request):
    return render(request, "components-spinners.html")


def components_tabs(request):
    return render(request, "components-tabs.html")


def components_tooltips(request):
    return render(request, "components-tooltips.html")


def forms_editors(request):
    return render(request, "forms-editors.html")


def forms_elements(request):
    return render(request, "forms-elements.html")


def forms_layouts(request):
    return render(request, "forms-layouts.html")


def forms_validation(request):
    return render(request, "forms-validation.html")


def icons_bootstrap(request):
    return render(request, "icons-bootstrap.html")


def icons_boxicons(request):
    return render(request, "icons-boxicons.html")


def icons_remix(request):
    return render(request, "icons-remix.html")


def pages_blank(request):
    return render(request, "pages-blank.html")


def pages_contact(request):
    return render(request, "pages-contact.html")


def pages_faq(request):
    return render(request, "pages-faq.html")


def pages_login(request):
    return render(request, "pages-login.html")


def pages_register(request):
    return render(request, "pages-register.html")


def tables_data(request):
    return render(request, "tables-data.html")


def tables_general(request):
    return render(request, "tables-general.html")


def users_profile(request):
    return render(request, "users-profile.html")
