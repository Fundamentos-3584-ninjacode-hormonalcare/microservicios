package com.innovasoft.remodify.platform.iam.application.internal.commandservices;

import com.innovasoft.remodify.platform.iam.application.internal.outboundservices.tokens.TokenService;
import com.innovasoft.remodify.platform.iam.domain.services.ValidateTokenCommandService;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class ValidaTokenCommandServiceImpl implements ValidateTokenCommandService {
    private final TokenService tokenService;

    public ValidaTokenCommandServiceImpl(TokenService tokenService) {
        this.tokenService = tokenService;
    }

    @Override
    public Optional<Boolean> handle(String token) {
        return Optional.of(tokenService.validateToken(token));
    }
}
