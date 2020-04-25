from django.conf import settings
import requests

# create CVAT realm
# requets.post('/auth/admin/realms', '{"enabled":true,"id":"CVAT","realm":"CVAT"}')

# update CVAT realm
# requests.put('/auth/admin/realms/CVAT', '{"id":"CVAT","realm":"CVAT","notBefore":0,"revokeRefreshToken":false,"refreshTokenMaxReuse":0,"accessTokenLifespan":300,"accessTokenLifespanForImplicitFlow":900,"ssoSessionIdleTimeout":1800,"ssoSessionMaxLifespan":36000,"ssoSessionIdleTimeoutRememberMe":0,"ssoSessionMaxLifespanRememberMe":0,"offlineSessionIdleTimeout":2592000,"offlineSessionMaxLifespanEnabled":false,"offlineSessionMaxLifespan":5184000,"accessCodeLifespan":60,"accessCodeLifespanUserAction":300,"accessCodeLifespanLogin":1800,"actionTokenGeneratedByAdminLifespan":43200,"actionTokenGeneratedByUserLifespan":300,"enabled":true,"sslRequired":"external","registrationAllowed":false,"registrationEmailAsUsername":false,"rememberMe":false,"verifyEmail":false,"loginWithEmailAllowed":true,"duplicateEmailsAllowed":false,"resetPasswordAllowed":false,"editUsernameAllowed":false,"bruteForceProtected":false,"permanentLockout":false,"maxFailureWaitSeconds":900,"minimumQuickLoginWaitSeconds":60,"waitIncrementSeconds":60,"quickLoginCheckMilliSeconds":1000,"maxDeltaTimeSeconds":43200,"failureFactor":30,"defaultRoles":["offline_access","uma_authorization"],"requiredCredentials":["password"],"otpPolicyType":"totp","otpPolicyAlgorithm":"HmacSHA1","otpPolicyInitialCounter":0,"otpPolicyDigits":6,"otpPolicyLookAheadWindow":1,"otpPolicyPeriod":30,"otpSupportedApplications":["FreeOTP","Google Authenticator"],"webAuthnPolicyRpEntityName":"keycloak","webAuthnPolicySignatureAlgorithms":["ES256"],"webAuthnPolicyRpId":"","webAuthnPolicyAttestationConveyancePreference":"not specified","webAuthnPolicyAuthenticatorAttachment":"not specified","webAuthnPolicyRequireResidentKey":"not specified","webAuthnPolicyUserVerificationRequirement":"not specified","webAuthnPolicyCreateTimeout":0,"webAuthnPolicyAvoidSameAuthenticatorRegister":false,"webAuthnPolicyAcceptableAaguids":[],"webAuthnPolicyPasswordlessRpEntityName":"keycloak","webAuthnPolicyPasswordlessSignatureAlgorithms":["ES256"],"webAuthnPolicyPasswordlessRpId":"","webAuthnPolicyPasswordlessAttestationConveyancePreference":"not specified","webAuthnPolicyPasswordlessAuthenticatorAttachment":"not specified","webAuthnPolicyPasswordlessRequireResidentKey":"not specified","webAuthnPolicyPasswordlessUserVerificationRequirement":"not specified","webAuthnPolicyPasswordlessCreateTimeout":0,"webAuthnPolicyPasswordlessAvoidSameAuthenticatorRegister":false,"webAuthnPolicyPasswordlessAcceptableAaguids":[],"browserSecurityHeaders":{"contentSecurityPolicyReportOnly":"","xContentTypeOptions":"nosniff","xRobotsTag":"none","xFrameOptions":"SAMEORIGIN","contentSecurityPolicy":"frame-src 'self'; frame-ancestors 'self'; object-src 'none';","xXSSProtection":"1; mode=block","strictTransportSecurity":"max-age=31536000; includeSubDomains"},"smtpServer":{},"eventsEnabled":false,"eventsListeners":["jboss-logging"],"enabledEventTypes":[],"adminEventsEnabled":false,"adminEventsDetailsEnabled":false,"internationalizationEnabled":false,"supportedLocales":[],"browserFlow":"browser","registrationFlow":"registration","directGrantFlow":"direct grant","resetCredentialsFlow":"reset credentials","clientAuthenticationFlow":"clients","dockerAuthenticationFlow":"docker auth","attributes":{},"userManagedAccessAllowed":true,"displayName":"Computer Vision Annotation Tool"}')

# create server-rest-api client
# requests.post('/auth/admin/realms/CVAT/clients', '{"enabled":true,"attributes":{},"redirectUris":[],"clientId":"server-rest-api","rootUrl":"http://localhost:8080/api/v1/","protocol":"openid-connect"}')

# update server-rest-api client
# requests.put('/auth/admin/realms/CVAT/clients/c86407d8-029e-47cb-b18f-4fc73593189a', '{"id":"c86407d8-029e-47cb-b18f-4fc73593189a","clientId":"server-rest-api","rootUrl":"http://localhost:8080/api/v1/","adminUrl":"http://localhost:8080/api/v1/","surrogateAuthRequired":false,"enabled":true,"alwaysDisplayInConsole":false,"clientAuthenticatorType":"client-secret","redirectUris":["http://localhost:8080/api/v1/*"],"webOrigins":["http://localhost:8080"],"notBefore":0,"bearerOnly":false,"consentRequired":false,"standardFlowEnabled":true,"implicitFlowEnabled":false,"directAccessGrantsEnabled":true,"serviceAccountsEnabled":true,"publicClient":false,"frontchannelLogout":false,"protocol":"openid-connect","attributes":{"saml.server.signature":"false","saml.server.signature.keyinfo.ext":"false","saml.assertion.signature":"false","saml.client.signature":"false","saml.encrypt":"false","saml.authnstatement":"false","saml.onetimeuse.condition":"false","saml_force_name_id_format":"false","saml.multivalued.roles":"false","saml.force.post.binding":"false","exclude.session.state.from.auth.response":"false","tls.client.certificate.bound.access.tokens":"false","display.on.consent.screen":"false"},"authenticationFlowBindingOverrides":{},"fullScopeAllowed":true,"nodeReRegistrationTimeout":-1,"defaultClientScopes":["web-origins","role_list","profile","roles","email"],"optionalClientScopes":["address","phone","offline_access","microprofile-jwt"],"access":{"view":true,"configure":true,"manage":true},"authorizationServicesEnabled":true}')

# delete default resource
# requests.delete('/auth/admin/realms/CVAT/clients/c86407d8-029e-47cb-b18f-4fc73593189a/authz/resource-server/resource/72e5f1e8-2545-41c1-b5ac-52833ee62e8b')

# delete default policy
# requests.delete('/auth/admin/realms/CVAT/clients/c86407d8-029e-47cb-b18f-4fc73593189a/authz/resource-server/policy/0efbffac-c6aa-4d52-8b2f-d46094005851')

