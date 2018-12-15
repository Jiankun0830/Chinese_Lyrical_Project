/*jslint browser: true*/
/*global $*/

$(document).ready(function () {
  $('#example').DataTable({
    bProcessing: true,
    bServerSide: true,
    sPaginationType: "full_numbers",
    lengthMenu: [[10, 25, 50, 100], [10, 25, 50, 100]],
    bjQueryUI: true,
    sAjaxSource: '/serverside_table',
    columns: [
        {"data": "product_code"},
        {"data": "product_category"},
        {"data": "item_id"},
        {"data": "has_serial_number"},
        {"data": "product_name"},
        {"data": "is_supported"},
        {
          "data": "product_image_name",
          "render": function ( data, type, row, meta ) {
              if(data!=null){
              return '<a href="https://s3.amazonaws.com/rzrwarranty/'+data+'" target="_blank"><img src="https://s3.amazonaws.com/rzrwarranty/'+data+'" width="240" height="171" border="0"></a>';
              }
          }
        },
        {
          "data": "product_code",
          "render": function(data, type, row, meta){
            return '<a href="/modify/'+data+'" class="btn btn-default">Edit</a>';
          }
        },
        {
          "data": "product_code",
          "render": function(data, type, row, meta){
            return '<form action="/deletecode/'+data+'" method="POST"><input type="submit" onclick="return clicked();" value="delete" class="btn btn-danger"/></form>'
          }
        }
    ]
  });
});
    function clicked() {
       if (confirm('Do you want to delete?')) {
           yourformelement.submit();
       } else {
           return false;
       }
    }
setInterval( function () {
    table.ajax.reload();
}, 30000 );