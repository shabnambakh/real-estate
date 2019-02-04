var urls = {
    "getApartmentList": "/api/apartments",
    "getOptionList": "/api/options",
    "getCityList": "/api/cities"
};

var rooms_types = {
    'studio': 'Студия',
    '1': '1-комнатная квартира',
    '2': '2-комнатная квартира',
    '3': '3-комнатная квартира',
    '4': '4-комнатная квартира',
    '5': '5-комнатная квартира',
    '6': '6-комнатная квартира',

}
var balcony_types = {
    '1b': 'Балкон',
    '1l': 'Лоджия',
    '1b1l': 'Балкон и лоджия'
}

$(document).ready(function() {
    initOptions();
    initCities();
    $('#submit').on('click', function(){
        getList();
    });
});


function getList() {
    var url = urls['getApartmentList'] + '?' + getArgs();

    $('#apartmentList').html("");

    $.getJSON(url, function (resp) {
        $.each(resp.results, function (index, apartment) {
            var card = $("<article class='card mb-4 box-shadow'>");
            var mortgage = apartment.mortgage ? 'есть': 'нет';
            var army_mortgage = apartment.army_mortgage ? 'есть': 'нет';

            text = 'Кол-во комнат: ' + rooms_types[apartment.rooms] + '</br>' +
                    'Город: ' + apartment.city.name + '</br>' +
                    'Тип балкона: ' + balcony_types[apartment.balcony_type] + '</br>' +
                    'Цена: ' + apartment.price + '</br>' +
                    'Площадь: ' + apartment.area + '</br>' +
                    'Ипотека: ' + mortgage + '</br>' +
                    'Военная ипотека: ' + army_mortgage;
            card.html(text);


            card.appendTo( "#apartmentList" );
        });
    });
}

function getArgs(){
    price_range = $("#price_range").slider("getValue");
    area_range = $("#area_range").slider("getValue");

    args = {}
    args['rooms'] = $("#rooms").val().join();
    args['city'] = $("#city").val();
    args['balcony_type'] = $("#balcony_type").val().join();
    args['price_min'] = price_range[0];
    args['price_max'] = price_range[1];
    args['area_min'] = area_range[0];
    args['area_max'] = area_range[1];

    if ($('#mortgage').is(":checked")){
        args['mortgage'] = '1';
    }
    if ($('#army_mortgage').is(":checked")){
        args['army_mortgage'] = '1';
    }
    return $.param(args)
}

function changeCount() {
    var url = urls['getOptionList'] + '?' + getArgs();

    $.getJSON(url, function (resp) {
        $('#count').text(resp.results.count);
        $("#price_range").slider({min:resp.results.min_price,
            max:resp.results.max_price,
            value:[resp.results.min_price, resp.results.max_price],
            range:true});
        $("#area_range").slider({min:resp.results.min_area,
            max:result.max_area,
            value:[resp.results.min_area, resp.results.max_area],
            range:true});

        $('#min_price').text(resp.results.min_price);
        $('#max_price').text(resp.results.max_price);
        $('#totalPrice').text('(' + resp.results.min_price + ' - ' + resp.results.max_price + ')');
        $('#min_area').html(resp.results.min_area + "м<sup>2</sup>");
        $('#max_area').html(resp.results.max_area + "м<sup>2</sup>");
        $('#totalArea').html('(' + resp.results.min_area + "м<sup>2</sup> - " + resp.results.max_area + 'м<sup>2</sup>)');
    });

}

function initOptions() {
    var url = urls['getOptionList'];
    $.getJSON(url, function (resp) {
        result = resp.results;
        $("#price_range").slider({min:result.min_price,
            max:result.max_price,
            value:[result.min_price, result.max_price],
            range:true}).on('change', function(){
                values = $("#price_range").slider("getValue");

                $('#totalPrice').text('(' + values[0] + ' - ' + values[1] + ')');
                changeCount();

            });

        $("#area_range").slider({min:result.min_area,
            max:result.max_area,
            value:[result.min_area, result.max_area],
            range:true}).on('change', function(){
                values = $("#area_range").slider("getValue");

                $('#totalArea').html('(' + values[0] + "м<sup>2</sup> - " + values[1] + 'м<sup>2</sup>)');
                changeCount();

            });
        $('#rooms').change(function(){
            changeCount();
        });
        $('#balcony_type').change(function(){
            changeCount();
        });
        $('#mortgage').change(function(){
            changeCount();
        });
        $('#army_mortgage').change(function(){
            changeCount();
        });
        $('#city').change(function(){
            changeCount();
        });

        $('#min_price').text(result.min_price);
        $('#max_price').text(result.max_price);
        $('#totalPrice').text('(' + result.min_price + ' - ' + result.max_price + ')');
        $('#min_area').html(result.min_area + "м<sup>2</sup>");
        $('#max_area').html(result.max_area + "м<sup>2</sup>");
        $('#totalArea').html('(' + result.min_area + "м<sup>2</sup> - " + result.max_area + 'м<sup>2</sup>)');
        $('#count').text(result.count);
    });

}

function initCities(){
    var url = urls['getCityList'];

    $('#city').html("<option value=''>");

    $.getJSON(url, function (resp) {
        $.each(resp.results, function (index, city) {
            var option = $("<option value='" + city.id + "'>");
            option.html(city.name);

            option.appendTo( "#city" );
        });
    });
}
