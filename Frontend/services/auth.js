blankApp
   .factory('Auth', ['$http', '$localStorage', 'urls', function ($http, $localStorage, urls) {
       function urlBase64Decode(str) {
           var output = str.replace('-', '+').replace('_', '/');
           switch (output.length % 4) {
               case 0:
                   break;
               case 2:
                   output += '==';
                   break;
               case 3:
                   output += '=';
                   break;
               default:
                   throw 'Illegal base64url string!';
           }
           return window.atob(output);
       }

       function getClaimsFromToken() {
           var token = $localStorage.token;
           var user = {};
           if (typeof token !== 'undefined') {
               var encoded = token.split('.')[1];
               user = JSON.parse(urlBase64Decode(encoded));
           }
           return user;
       }
       
       delete $localStorage.token;
       var tokenClaims = getClaimsFromToken();

       return {
           signup: function (data, success, error) {
               $http.post(urls.BASE + '/rest-auth/registration/', data).success(success).error(error);
           },
           signin: function (data, success, error) {
               $http.post(urls.BASE + '/rest-auth/login/', data).success(success).error(error);
           },
           signout: function (success) {
               $http.post(urls.BASE + '/rest-auth/logout/', data);
               tokenClaims = {};
               delete $localStorage.token;
               success();
           },
           getTokenClaims: function () {
               return tokenClaims;
           },
       };
   }
   ]);

