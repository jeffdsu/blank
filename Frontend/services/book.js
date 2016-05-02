blankApp.service('bookService', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;
    self.id = null;
    self.insights = null;
    
    self.get_collection = function () {
        return $http.get(urls.BASE + "/inspiration-corner/books")
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
        return $http.get(urls.BASE + "/inspiration-corner/books/" + id)
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

    self.get_insights = function (id) {
        return $http.get(urls.BASE + "/inspiration-corner/books/" + id + "/insights")
            .then(function (response) {
                if (typeof response.data === 'object') {
                    self.insights = response.data
                    return response.data;
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            });
    };
    
    self.get_top_10_keywords = function(id) {
        return $http.get(urls.BASE + "/inspiration-corner/books/" + id + "/keywords?style='top_10'")
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
    
    self.add_insight = function (insight) {
        return $http.post(urls.BASE + "/inspiration-corner/books/" + self.id + "/insights", insight)
            .then(function (response) {
                if (typeof response.data === 'object') {
                    self.insights.push(response.data);
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            });
    };
    
    self.get_random_insight = function (id) {
        return $http.get(urls.BASE + "/inspiration-corner/books/" + id + "/insights?random_top_10=true")
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