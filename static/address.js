function save_address(fname, iname) {
    document.forms[fname].action = '/customer/center/address_save_' + iname;
    document.forms[fname].method = 'POST';
    document.forms[fname].submit();
}

function delete_address(fname, iname) {
    document.forms[fname].action = '/customer/center/address_del_' + iname;
    document.forms[fname].method = 'POST';
    document.forms[fname].submit();

}