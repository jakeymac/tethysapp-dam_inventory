var notification_ws = new WebSocket('ws://' + window.location.host + '/apps/dam-inventory/dams/notifications/ws/');
var n_div = $("#notification");
var n_title = $("#notificationLabel");
var n_content = $('#notification .lead');

notification_ws.onmessage = function (e) {
    var data = JSON.parse(e.data);
    if (data["message"] = "New Dam") {
        n_title.html('Dam Notification');
        n_content.html('A new dam has been added. Refresh this page to load it.');
        n_div.modal('show');
        TETHYS_APP_BASE.alert('success', 'A new dam has been added. Refresh this page to load it.');
    }
};