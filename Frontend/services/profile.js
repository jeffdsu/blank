blankApp.service('profileService', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;

    self.get = function (id) {
        return $http.get(urls.BASE + "/inspiration-corner/profile/" + id)
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
    
    self.get_insights = function (personal) {
        return $http.get(urls.BASE + "/inspiration-corner/profile/insights?personal=" + personal)
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