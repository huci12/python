nMap = {
    mapContainer: null,
    map: null,
    initLat: null,
    initLong: null,
    initLevel: null,

    init: function(container, x, y, level) {
        if (level == undefined) {
            this.initLevel = 3;
        } else {
            this.initLevel = level;
        }

        if (x == undefined || y == undefined) {
            this.getClientLocation().then((position) => {
                this.setLatLang(position.coords.latitude, position.coords.longitude)
                this.createMap(container)
            }).catch((err) => {
                console.error(err.message);
                this.setLatLang(33.450701, 126.570667);
                this.createMap(container)
            })
        } else {
            this.initLat = x;
            this.initLong = y;
            this.createMap(container)
        }
    },

    createMap: function(container) {
        this.mapContainer = document.getElementById(container);
        var mapOption = {
            center: new kakao.maps.LatLng(this.initLat, this.initLong), // 지도의 중심좌표
            level: this.level // 지도의 확대 레벨
        };

        // 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
        this.map = new kakao.maps.Map(this.mapContainer, mapOption);
    },

    setLatLang: function(x, y) {
        this.initLat = x;
        this.initLong = y;
    },

    getClientLocation: function(options) {
        return new Promise(function(resolve, reject, options) {
            navigator.geolocation.getCurrentPosition(resolve, reject, options);
        });
    }
}