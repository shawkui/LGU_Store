function minus_amt(amt, price, cost) {
    var x = parseFloat(document.getElementById(amt).value) - 1;
    var reg = /(^[1-9]\d*$)/
    if (!reg.test(x)) {
        alert('Must be positive integer！');
        return false
    }
    document.getElementById(amt).value = x;
    document.getElementById(cost).innerHTML = (price * parseFloat(document.getElementById(amt).value)).toFixed(2);
    return true;

}

function add_amt(amt, price, cost) {
    var x = parseFloat(document.getElementById(amt).value) + 1;
    var reg = /(^[1-9]\d*$)/
    if (!reg.test(x)) {
        alert('Must be positive integer！');
        return false
    }
    document.getElementById(amt).value = x;
    document.getElementById(cost).innerHTML = (price * parseFloat(document.getElementById(amt).value)).toFixed(2);
    return true;

}

function update_cost(amt, price, cost) {
    var x = parseFloat(document.getElementById(amt).value);
    var reg = /(^[1-9]\d*$)/
    if (!reg.test(x)) {
        alert('Must be positive integer！');
        return false
    }
    document.getElementById(cost).innerHTML = (price * parseFloat(document.getElementById(amt).value)).toFixed(2);
    return true;

}

function save_item(fname, iname) {
    document.forms[fname].action = '/customer/center/shoppingcart_save_' + iname;
    document.forms[fname].method = 'POST';
    document.forms[fname].submit();
}

function delete_item(fname, iname) {
    document.forms[fname].action = '/customer/center/shoppingcart_del_' + iname;
    document.forms[fname].method = 'POST';
    document.forms[fname].submit();

}
