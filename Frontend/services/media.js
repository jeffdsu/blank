blankApp.service('mediaService', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;
    self.id = null;
    self.insights = null;
    self.mediaType = null;

    self.get_collection = function () {
        return $http.get(urls.BASE + "/inspiration-corner/media/" + this.mediaType)
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
        return $http.get(urls.BASE + "/inspiration-corner/media/" + this.mediaType + "/" + id)
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

    self.create = function (data) {
        return $http.post(urls.BASE + "/inspiration-corner/media/" + this.mediaType, data)
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
        return $http.get(urls.BASE + "/inspiration-corner/media/" + this.mediaType + "/" + id + "/insights")
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

    self.get_top_10_keywords = function (id) {
        return $http.get(urls.BASE + "/inspiration-corner/media/" + this.mediaType + "/" + id + "/keywords?style=top_10")
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

    self.add_insight = function (medium, insight) {
        return $http.post(urls.BASE + "/inspiration-corner/media/" + medium.type.name + "/" + medium.id + "/insights", insight)
            .then(function (response) {
                if (typeof response.data === 'object') {
                    self.insights.push(response.data);
                    return response.data;
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            });
    };

    self.get_random_insight = function (id, keyword_filter) {

        url = urls.BASE + "/inspiration-corner/media/" + this.mediaType + "/" + id + "/insights?random_top_10=true";
        if (keyword_filter) {
            search_words = keyword_filter.split(" ");

            angular.forEach(search_words, function (word) {
                url += "&keywords_filter=" + word;
            });
        }

        return $http.get(url)
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