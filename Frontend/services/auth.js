blankApp.service('Auth', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;
    
    self.is_logged_in = function() {
        console.log($localStorage.logged_in);
        if ($localStorage.logged_in) {return true;}
        return false;
    };
   
   self.signin = function (data) {
        return $http.post(urls.BASE + '/rest-auth/login/', data)
            .then(function (response) {
                $localStorage.token = response.key;
               $localStorage.logged_in = true;
               return response.data;
                
            }, function (response) {
                return $q.reject(response.data)
            });

    };
    
    
    self.signout = function () {
        return $http.post(urls.BASE + '/rest-auth/logout/')
            .then(function (response) {
                if (typeof response.data === 'object') {
                    $localStorage.token = null;
                    $localStorage.logged_in = false;
                    return response.data;
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            });

    };
    
    self.signup = function (data) {
        return $http.post(urls.BASE + '/rest-auth/registration/', data)
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
    
    self.sign_in_fb = function (authResponse) {
        
        data = { access_token: authResponse.accessToken, backend:"facebook"}
        
        return $http.post(urls.BASE + '/inspiration-corner/api/auth', data)
            .then(function (response) {
                if (typeof response.data === 'object') {
                    $localStorage.logged_in = true;
                    $localStorage.token = response.key;
                    return response.data
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            });

    };
    
    
}]);
