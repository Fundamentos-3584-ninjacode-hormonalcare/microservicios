package com.innovasoft.remodify.platform.iam.domain.services;

import com.innovasoft.remodify.platform.iam.domain.model.commands.SeedRolesCommand;

public interface RoleCommandService {
    void handle(SeedRolesCommand command);
}
