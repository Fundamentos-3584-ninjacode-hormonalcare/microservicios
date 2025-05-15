package com.innovasoft.remodify.platform.profiles.interfaces.rest.transform;

import com.innovasoft.remodify.platform.profiles.domain.model.aggregates.Profile;
import com.innovasoft.remodify.platform.profiles.interfaces.rest.resources.ProfileResource;

public class ProfileResourceFromEntityAssembler {
    public static ProfileResource toResourceFromEntity(Profile entity){
        return new ProfileResource(
                entity.getId(),
                entity.getEmailAddress(),
                entity.getPassword(),
                entity.getType(),
                entity.getFullName()
        );
    }
}
