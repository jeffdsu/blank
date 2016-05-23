blankApp.service('contributorService', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;

    self.get_collection = function () {
        return $http.get(urls.BASE + "/inspiration-corner/contributors")
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

    self.get = function (id) {
        return $http.get(urls.BASE + "/inspiration-corner/contributors/" + id)
            .then(function (response) {
                if (typeof response.data === 'object') {
                    return response.data
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            })
    };
    
    self.get_books = function (id) {
        return $http.get(urls.BASE + "/inspiration-corner/contributors/" + id + "/works")
            .then(function (response) {
                if (typeof response.data === 'object') {
                    return response.data
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            })
    };

}]);