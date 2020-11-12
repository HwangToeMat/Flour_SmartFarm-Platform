package com.example.flour.repository;

import com.example.flour.model.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.NoRepositoryBean;
import org.springframework.stereotype.Repository;

@Repository
@NoRepositoryBean
public interface UserRepository extends JpaRepository<User, Long> {
}
