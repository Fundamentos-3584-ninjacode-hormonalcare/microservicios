package com.innovasoft.remodify.platform.iam.interfaces.rest.transform;

import com.innovasoft.remodify.platform.iam.domain.model.entities.Role;
import com.innovasoft.remodify.platform.iam.interfaces.rest.resources.RoleResource;

public class RoleResourceFromEntityAssembler {
    public static RoleResource toResourceFromEntity(Role entity) {
        return new RoleResource(entity.getId(), entity.getStringName());
    }
}
