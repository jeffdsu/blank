blankApp.service('baseService', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;
    
    self.get_collection = function () {
        return $http.get(urls.BASE + "/inspiration-corner/authors")
            .then(function (response) {
                if (typeof response.data === 'object') {
                    return response.data
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            });

    };
}]);