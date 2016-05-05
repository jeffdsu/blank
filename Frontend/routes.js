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
        })
        .when('/signout', {
            templateUrl: 'partials/signout.htm'
            , controller: 'authController'
        })
        .when('/signup', {
            templateUrl: 'partials/signup.htm'
            , controller: 'authController'
        })
        .when('/admin/inspiration/words-to-ignore', {
            templateUrl: 'partials/admin-words-to-ignore.htm'
            , controller: 'adminWordsToIgnoreController'
        })
        .when('/inspiration/authors', {
            templateUrl: 'partials/authors.htm'
            , controller: 'authorsController'
        })
        .when('/inspiration/authors/:authorId', {
            templateUrl: 'partials/author-details.htm'
            , controller: 'authorDetailsController'
        })
        .when('/inspiration/users/:userId', {
            templateUrl: 'partials/user-details.htm'
            , controller: 'userDetailsController'
        });

}]);