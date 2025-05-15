package com.innovasoft.remodify.platform.iam.interfaces.rest.transform;

import com.innovasoft.remodify.platform.iam.domain.model.aggregates.User;
import com.innovasoft.remodify.platform.iam.domain.model.entities.Role;
import com.innovasoft.remodify.platform.iam.interfaces.rest.resources.UserResource;

public class UserResourceFromEntityAssembler {
    public static UserResource toResourceFromEntity(User entity) {
        var roles = entity.getRoles().stream().map(Role::getStringName).toList();
        return new UserResource(entity.getId(), entity.getUsername(), roles, entity.getEmail(), entity.getFirstName(), entity.getPaternalSurname(), entity.getMaternalSurname(), entity.getDescription(), entity.getPhone(), entity.getImage());
    }
}
