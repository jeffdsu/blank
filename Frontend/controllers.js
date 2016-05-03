blankApp.controller('booksController', ['$scope', '$resource', '$routeParams', '$http', '$interval', 'bookService', 'insightService', function ($scope, $resource, $routeParams, $http, $interval, bookService, insightService) {

    var insights_interval;
    //var $scope.top_10_words = {};



    $scope.get_random_insight_for_each_book = function () {

        angular.forEach($scope.books, function (value, key) {
            bookService.get_random_insight(value.id)
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
                                value.keywords[data[i].word] = [i+1, data[i]];
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


blankApp.controller('inspirationController', ['$scope', '$resource', '$routeParams', '$http', 'mediumService', function ($scope, $resource, $routeParams, $http, mediumService) {


    mediumService.get_collection()
        .then(function (data) {
                $scope.mediums = data;
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
            , book: bookService.id
        };

        bookService.add_insight(formData)
            .then(function () {
                $scope.dialogShown = !$scope.dialogShown;
            })
    }

}]);

blankApp.controller('authController', ['urls', '$rootScope', '$scope', '$resource', '$routeParams', '$http', '$localStorage', '$location', 'Auth', function (urls, $rootScope, $scope, $resource, $routeParams, $http, $localStorage, $location, Auth) {


    function successAuth(res) {
        $localStorage.token = res.token;
        $location.path('inspiration').replace();
    }

    $scope.signin = function () {

        var formData = {
            username: $scope.username
            , password: $scope.password
        };

        Auth.signin(formData, successAuth, function () {
            console.log(urls.BASE);
            $rootScope.error = 'Invalid credentials.';
        })
    };

    $scope.logout = function () {
        Auth.logout(function () {
            window.location = "/"
        });
    };

}]);