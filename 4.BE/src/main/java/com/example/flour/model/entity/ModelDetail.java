package com.example.flour.model.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

import javax.persistence.*;
import java.time.LocalDateTime;

@NoArgsConstructor
@AllArgsConstructor
@Data
@Entity
@ToString(exclude = {"model", "subscribeList"})
public class ModelDetail {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String status;

    private LocalDateTime registeredAt;

    private LocalDateTime unregisteredAt;

    private LocalDateTime updatedAt;

    private String updatedBy;

    private Long subscribeListId;

    @ManyToOne
    private Model model;

    @ManyToOne
    private SubscribeList subscribeList;

}
