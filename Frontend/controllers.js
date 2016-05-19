blankApp.controller('booksController', ['$scope', '$resource', '$routeParams', '$http', '$interval', 'bookService', 'insightService', function ($scope, $resource, $routeParams, $http, $interval, bookService, insightService) {

    var insights_interval;
    //var $scope.top_10_words = {};



    $scope.get_random_insight_for_each_book = function () {

        angular.forEach($scope.books, function (value, key) {
            bookService.get_random_insight(value.id, $scope.query)
                .then(function (data) {
                    value.insight = data;
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


    bookService.get_collection()
        .then(function (data) {
                $scope.books = data;
                $scope.get_random_insight_for_each_book();
                if (angular.isDefined(insights_interval)) return;
                insights_interval = $interval($scope.get_random_insight_for_each_book, 5000);

                angular.forEach($scope.books, function (value, key) {
                    bookService.get_top_10_keywords(value.id)
                        .then(function (data) {
                            value.keywords = {}
                            for (i = 0; i < data.length; i++) {
                                value.keywords[data[i].word] = [i + 1, data[i]];
                            }
                        }, function (err) {

                        })
                });


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

blankApp.controller('booksDetailController', ['$scope', '$resource', '$routeParams', '$http', 'bookService', function ($scope, $resource, $routeParams, $http, bookService) {

    $scope.dialogShown = false;
    bookService.id = $routeParams.bookId;

    bookService.get($routeParams.bookId)
        .then(function (data) {
            $scope.book = data;
        }, function (err) {

        });

    bookService.get_insights($routeParams.bookId)
        .then(function (data) {
            $scope.insights = data;
        }, function (err) {


        });

    $scope.add_insight_modal = function () {
        console.log($scope.dialogShown);
        $scope.dialogShown = !$scope.dialogShown;
    }


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

blankApp.controller('addInsightController', ['$scope', '$resource', '$routeParams', '$http', 'bookService', function ($scope, $resource, $routeParams, $http, bookService) {


    $scope.add_insight = function (insight) {

        var formData = {
            lesson: insight
        };

        bookService.add_insight($routeParams.bookId, formData)
            .then(function () {
                $scope.dialogShown = !$scope.dialogShown;
            })
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
        $localStorage.token = res.key;
        $location.path('inspiration').replace();

    }


    $scope.signin = function () {

        var formData = {
            username: $scope.username
            , password: $scope.password
        };

        Auth.signin(formData, successAuth, function (err) {

            errorService.error = 'Invalid credentials.';
        })
    };

    $scope.signup = function () {

        var formData = {
            "username": $scope.username
            , "password1": $scope.password1
            , "password2": $scope.password2
            , "email": $scope.email
        };

        Auth.signup(formData
            , function () {
                $location.path('signin').replace();
            }
            , function (err) {

                errorService.error = 'Invalid credentials.';
            })
    }

    $scope.logout = function () {
        Auth.logout(function () {
            window.location = "/"
        });
    };


}]);