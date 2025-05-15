package com.innovasoft.remodify.platform.iam.domain.services;

import com.innovasoft.remodify.platform.iam.domain.model.aggregates.User;
import com.innovasoft.remodify.platform.iam.domain.model.queries.GetAllUsersQuery;
import com.innovasoft.remodify.platform.iam.domain.model.queries.GetUserByIdQuery;
import com.innovasoft.remodify.platform.iam.domain.model.queries.GetUserByUsernameQuery;

import java.util.List;
import java.util.Optional;

public interface UserQueryService {
    List<User> handle(GetAllUsersQuery query);
    Optional<User> handle(GetUserByIdQuery query);
    Optional<User> handle(GetUserByUsernameQuery query);
}
