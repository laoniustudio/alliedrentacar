/**
 * Created by sun on 7/18/2017.
 */

var alliedApp = angular
                        .module('allied',[])
                        .controller("alliedController",function ($scope,$http) {
                            // get func
                            $http.get("/api/get")
                                .then(function (response) {
                                    $scope.posts = response.data;
                                });
                            // // post func
                            //  var data = $.param({
                            //     fName: $scope.firstName,
                            //     lName: $scope.lastName
                            // });
                            //
                            // var config = {
                            //     headers : {
                            //         'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                            //     }
                            // }
                            //
                            // $http.post('/ServerRequest/PostDataResponse', data, config)
                            // .success(function (data, status, headers, config) {
                            //     $scope.PostDataResponse = data;
                            // })
                        });

