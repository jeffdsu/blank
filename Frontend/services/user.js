blankApp.service('userService', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;

    self.get = function (id) {
        return $http.get(urls.BASE + "/inspiration-corner/users/" + id)
            .then(function (response) {
                if (typeof response.data === 'object') {
                    return response.data;
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            });
    }
    
    self.get_insights = function (id) {
        return $http.get(urls.BASE + "/inspiration-corner/users/" + id + "/insights")
            .then(function (response) {
                if (typeof response.data === 'object') {
                    return response.data;
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            });
    };

}]);