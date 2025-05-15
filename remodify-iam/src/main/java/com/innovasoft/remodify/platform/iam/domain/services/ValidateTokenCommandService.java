package com.innovasoft.remodify.platform.iam.domain.services;

import java.util.Optional;

public interface ValidateTokenCommandService {
    Optional<Boolean> handle(String token);
}
