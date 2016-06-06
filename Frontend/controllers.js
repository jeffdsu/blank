blankApp.controller('mediaController', ['$scope', '$resource', '$routeParams', '$http', '$interval', 'mediaService', 'insightService', function ($scope, $resource, $routeParams, $http, $interval, mediaService, insightService) {

    var insights_interval;
    $scope.checked = 'I';
    $scope.mediaType = $routeParams.mediaType;
    mediaService.mediaType = $scope.mediaType;



    $scope.get_random_insight_for_each_book = function () {

        angular.forEach($scope.books, function (value, key) {
            mediaService.get_random_insight(value.id, $scope.query)
                .then(function (data) {
                    console.log(data);
                    value.insight = data[0];
                }, function (err) {

                })
        });
    };

    $scope.stop_getting_of_insights = function () {
        if (angular.isDefined(insights_interval)) {
            console.log("HEREERERER");
            $interval.cancel(insights_interval);
        }
    }


    mediaService.get_collection()
        .then(function (data) {
                $scope.books = data;
                $scope.get_random_insight_for_each_book();
                if (angular.isDefined(insights_interval)) return;
                insights_interval = $interval($scope.get_random_insight_for_each_book, 5000);

            }
            , function (err) {

            }
        );

    $scope.$on('$destroy', function () {
        $scope.stop_getting_of_insights();
    });
}]);


blankApp.controller('inspirationController', ['$scope', '$resource', '$routeParams', '$http', 'mediumTypeService', function ($scope, $resource, $routeParams, $http, mediumTypeService) {


    mediumTypeService.get_collection()
        .then(function (data) {
                $scope.mediums_types = data;
            }
            , function (err) {

            }
        );


}]);

blankApp.controller('navController', ['$scope', '$resource', '$routeParams', '$http', '$location', 'Auth', function ($scope, $resource, $routeParams, $http, $location, Auth) {

    $scope.signout = function () {
        Auth.signout(function () {
            $location.path('signin').replace();
        });
    };
   


}]);

blankApp.controller('mediaDetailController', ['$scope', '$resource', '$routeParams', '$http', 'mediaService', function ($scope, $resource, $routeParams, $http, mediaService) {


    $scope.mediaType = $routeParams.mediaType;
    mediaService.mediaType = $scope.mediaType;
    


    $scope.dialogShown = false;
    mediaService.id = $routeParams.mediaId;
    

    mediaService.get($routeParams.mediaId)
        .then(function (data) {
            $scope.book = data;
        }, function (err) {

        });

    mediaService.get_insights($routeParams.mediaId)
        .then(function (data) {
            $scope.insights = data;
        }, function (err) {


        });




}]);

blankApp.controller('signInController', ['$scope', '$resource', '$routeParams', '$http', function ($scope, $resource, $routeParams, $http) {

    $http.get("http://127.0.0.1:8000/inspiration-corner/books")
        .success(function (data, status, headers, config) {
            console.log(status)
            $scope.booksResult = data;
        }).error(function (data, status, headers, config) {
            console.log(status);
        });

}]);

blankApp.controller('addInsightController', ['$scope', '$resource', '$routeParams', '$http', 'mediaService', function ($scope, $resource, $routeParams, $http, mediaService) {


    $scope.add_insight = function (insight) {

        var formData = {
            lesson: insight
        };
        
        
        mediaService.add_insight($scope.medium, formData)
            .then(function () {
                $scope.dialogShown = !$scope.dialogShown;
            })
    }
    
    $scope.add_insight_modal = function () {
        console.log($scope.dialogShown);
        $scope.dialogShown = !$scope.dialogShown;
    }

}]);

blankApp.controller('errorController', ['urls', '$rootScope', '$scope', '$resource', '$routeParams', '$http', '$localStorage', '$location', 'errorService', function (urls, $rootScope, $scope, $resource, $routeParams, $http, $localStorage, $location, errorService) {

    //$scope.error = errorService.error;

    //console.log(errorService);


    $scope.$watch('errorService.error', function (newVal, oldVal, scope) {
        if (newVal) {
            console.log("asdfasdfas");
            scope.error = "qwer";
        }
    });

}]);


blankApp.controller('authController', ['urls', '$rootScope', '$scope', '$resource', '$routeParams', '$http', '$localStorage', '$location', 'Auth', 'errorService', function (urls, $rootScope, $scope, $resource, $routeParams, $http, $localStorage, $location, Auth, errorService) {


    function successAuth(res) {
        console.log(res);
        $localStorage.token = res.key;
        $location.path('inspiration-corner').replace();

    }


    $scope.signin = function () {
        
        var formData = {
            username: $scope.username
            , password: $scope.password
        };
        Auth.signin(formData, successAuth, function (err) {
            console.log(err);
            errorService.error = 'Invalid credentials.';
        })
    };

    $scope.signup = function () {


        Auth.signup($scope.user_signup
            , function () {
                $location.path('signin').replace();
            }
            , function (err) {

                errorService.error = 'Invalid credentials.';
            })
    }



}]);