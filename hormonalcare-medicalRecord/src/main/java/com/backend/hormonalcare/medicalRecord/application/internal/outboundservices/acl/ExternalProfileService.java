package com.backend.hormonalcare.medicalRecord.application.internal.outboundservices.acl;

import com.backend.hormonalcare.medicalRecord.domain.model.valueobjects.ProfileId;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Date;
import java.util.Optional;

@Service
public class ExternalProfileService {
    private final RestTemplate restTemplate;
    private final String iamBaseUrl;

    public ExternalProfileService(RestTemplate restTemplate, @Value("${iam.service.url:http://localhost:8081/api/v1/profile}") String iamBaseUrl) {
        this.restTemplate = restTemplate;
        this.iamBaseUrl = iamBaseUrl;
    }

    public Optional<ProfileId> fetchProfileIdByPhoneNumber(String phoneNumber) {
        String url = iamBaseUrl + "/phoneNumber/" + phoneNumber;
        ResponseEntity<ProfileResource> response = restTemplate.getForEntity(url, ProfileResource.class);
        if (!response.getStatusCode().is2xxSuccessful() || response.getBody() == null) return Optional.empty();
        return Optional.of(new ProfileId(response.getBody().getId()));
    }

    public Optional<ProfileId> createProfile(String firstName, String lastName, String gender, String phoneNumber, String image, Date birthday, Long userId) {
        String url = iamBaseUrl;
        CreateProfileRequest request = new CreateProfileRequest(firstName, lastName, gender, phoneNumber, image, birthday, userId);
        ResponseEntity<ProfileResource> response = restTemplate.postForEntity(url, request, ProfileResource.class);
        if (!response.getStatusCode().is2xxSuccessful() || response.getBody() == null) return Optional.empty();
        return Optional.of(new ProfileId(response.getBody().getId()));
    }

    public boolean updateProfile(Long profileId, String firstName, String lastName, String gender, String phoneNumber, String image, Date birthday) {
        String url = iamBaseUrl + "/" + profileId;
        UpdateProfileRequest request = new UpdateProfileRequest(firstName, lastName, gender, phoneNumber, image, birthday);
        restTemplate.put(url, request);
        return true; // Puedes mejorar el control de errores según la respuesta
    }

    public Optional<ProfileDetails> fetchProfileDetails(Long profileId) {
        String url = iamBaseUrl + "/" + profileId;
        ResponseEntity<ProfileResource> response = restTemplate.getForEntity(url, ProfileResource.class);
        if (!response.getStatusCode().is2xxSuccessful() || response.getBody() == null) return Optional.empty();
        ProfileResource profile = response.getBody();
        return Optional.of(new ProfileDetails(
                profile.getId(),
                profile.getFullName(),
                profile.getImage(),
                profile.getGender(),
                profile.getPhoneNumber(),
                profile.getBirthday()
        ));
    }

    // DTOs locales para mapear la respuesta de IAM
    public static class ProfileResource {
        private Long id;
        private String fullName;
        private String image;
        private String gender;
        private String phoneNumber;
        private String birthday;
        // getters y setters
        public Long getId() { return id; }
        public String getFullName() { return fullName; }
        public String getImage() { return image; }
        public String getGender() { return gender; }
        public String getPhoneNumber() { return phoneNumber; }
        public String getBirthday() { return birthday; }
        public void setId(Long id) { this.id = id; }
        public void setFullName(String fullName) { this.fullName = fullName; }
        public void setImage(String image) { this.image = image; }
        public void setGender(String gender) { this.gender = gender; }
        public void setPhoneNumber(String phoneNumber) { this.phoneNumber = phoneNumber; }
        public void setBirthday(String birthday) { this.birthday = birthday; }
    }
    public static class CreateProfileRequest {
        private String firstName, lastName, gender, phoneNumber, image;
        private Date birthday;
        private Long userId;
        public CreateProfileRequest(String firstName, String lastName, String gender, String phoneNumber, String image, Date birthday, Long userId) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.gender = gender;
            this.phoneNumber = phoneNumber;
            this.image = image;
            this.birthday = birthday;
            this.userId = userId;
        }
        // getters y setters
    }
    public static class UpdateProfileRequest {
        private String firstName, lastName, gender, phoneNumber, image;
        private Date birthday;
        public UpdateProfileRequest(String firstName, String lastName, String gender, String phoneNumber, String image, Date birthday) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.gender = gender;
            this.phoneNumber = phoneNumber;
            this.image = image;
            this.birthday = birthday;
        }
        // getters y setters
    }
    public static class ProfileDetails {
        private Long id;
        private String fullName;
        private String image;
        private String gender;
        private String phoneNumber;
        private String birthday;
        public ProfileDetails(Long id, String fullName, String image, String gender, String phoneNumber, String birthday) {
            this.id = id;
            this.fullName = fullName;
            this.image = image;
            this.gender = gender;
            this.phoneNumber = phoneNumber;
            this.birthday = birthday;
        }

        public Long getId() { return id; }
        public String getFullName() { return fullName; }
        public String getImage() { return image; }
        public String getGender() { return gender; }
        public String getPhoneNumber() { return phoneNumber; }
        public String getBirthday() { return birthday; }
    }
}
