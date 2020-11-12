package com.example.flour.repository;

import com.example.flour.model.entity.SubscribeList;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.NoRepositoryBean;
import org.springframework.stereotype.Repository;

@Repository
@NoRepositoryBean
public interface SubscribeListRepository extends JpaRepository<SubscribeList, Long> {
}
