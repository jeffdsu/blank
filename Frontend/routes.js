blankApp.config(['$routeProvider', '$httpProvider', function ($routeProvider, $httpProvider) {

    $routeProvider

        .when('/', {
            templateUrl: 'partials/home.htm'
            , controller: 'homeController'
        })
        .when('/inspiration', {
            templateUrl: 'partials/inspiration.htm'
            , controller: 'inspirationController'
        })
        .when('/inspiration/books', {
            templateUrl: 'partials/books.htm'
            , controller: 'booksController'
        })
        .when('/inspiration/books/:bookId', {
            templateUrl: 'partials/book-details.htm'
            , controller: 'booksDetailController'
        })
        .when('/signin', {
            templateUrl: 'partials/signin.htm'
            , controller: 'authController'
        });

}]);