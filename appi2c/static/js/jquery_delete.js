$.confirm({
    useBootstrap: false,
    scrollToPreviousElementAnimate: false,
    draggable: false,
    bgOpacity: 0.90,
    boxWidth: '40%',
    icon: "far fa-grimace",
    title: 'Attention!',
    content: params['msg'],
    type: 'red',
    autoClose: 'cancel|10000',
    buttons: {
        ok: {
            text: "Ok",
            btnClass: 'btn-red',
            keys: ['enter'],
            action: function () {
                window.location.href = params['href'];
            }
        },
        cancel:{ 
            text: "Cancel",
            keys: ['esc'],
            action: function () {

            }
        },
    }
});