blankApp.service('mediaService', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;

    self.get_collection = function (medium_type) {
        
        medium_type_name = null;
        if (typeof medium_type === 'object') {
            medium_type_name = medium_type.name
        } 
        else {
            medium_type_name = medium_type
        }
        
        console.log(medium_type);
        
        return $http.get(urls.BASE + "/inspiration-corner/media/" + medium_type_name)
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

    self.get = function (medium_type, id) {
        
        medium_type_name = null;
        if (typeof medium_type === 'object') {
            medium_type_name = medium_type.name
        } 
        else {
            medium_type_name = medium_type
        }
        
        return $http.get(urls.BASE + "/inspiration-corner/media/" + medium_type_name + "/" + id)
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

    self.create = function (medium) {
        return $http.post(urls.BASE + "/inspiration-corner/media/" + medium.type.name, medium)
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
    
    self.update = function (medium) {
        return $http.put(urls.BASE + "/inspiration-corner/media/" + medium.type.name + "/" + medium.id, medium)
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

    self.get_insights = function (medium_type, id) {
        return $http.get(urls.BASE + "/inspiration-corner/media/" + medium_type.name + "/" + id + "/insights")
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
        
        console.log(insight);
        
        return $http.post(urls.BASE + "/inspiration-corner/media/" + medium.type.name + "/" + medium.id + "/insights", insight)
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
    
    self.add_personal_insight = function (medium, insight) {
        
        insight.personal = true;
        
        return $http.post(urls.BASE + "/inspiration-corner/media/" + medium.type.name + "/" + medium.id + "/insights", insight)
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

    self.get_random_insight = function (medium_type, id, keyword_filter) {
        
        medium_type_name = null;
        if (typeof medium_type === 'object') {
            medium_type_name = medium_type.name
        } 
        else {
            medium_type_name = medium_type
        }

        url = urls.BASE + "/inspiration-corner/media/" + medium_type_name + "/" + id + "/insights?random_top_10=true";
        if (keyword_filter) {
            search_words = keyword_filter.split(" ");

            angular.forEach(search_words, function (word) {
                url += "&keywords_filter=" + word;
            });
        }

        return $http.get(url)
            .then(function (response) {
                if (typeof response.data === 'object') {
                    console.log(response.data);
                    return response.data;
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            });
    };

}]);