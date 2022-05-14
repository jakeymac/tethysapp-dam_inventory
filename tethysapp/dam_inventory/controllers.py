from django.shortcuts import render, reverse
from tethys_sdk.gizmos import MapView, Button
from tethys_sdk.routing import controller


@controller
def home(request):
    """
    Controller for the app home page.
    """

    dam_inventory_map = MapView(
        height='100%',
        width='100%',
        layers=[],
        basemap=['OpenStreetMap'],
    )


    add_dam_button = Button(
        display_text='Add Dam',
        name='add-dam-button',
        icon='plus-square',
        style='success',
        href=reverse('dam_inventory:add_dam')
    )

    context = {
        'dam_inventory_map': dam_inventory_map,
        'add_dam_button': add_dam_button
    }

    return render(request, 'dam_inventory/home.html', context)


@controller(url='dams/add')
def add_dam(request):
    """
    Controller for the Add Dam page.
    """
    add_button = Button(
        display_text='Add',
        name='add-button',
        icon='plus-square',
        style='success'
    )

    cancel_button = Button(
        display_text='Cancel',
        name='cancel-button',
        href=reverse('dam_inventory:home')
    )

    context = {
        'add_button': add_button,
        'cancel_button': cancel_button,
    }

    return render(request, 'dam_inventory/add_dam.html', context)
