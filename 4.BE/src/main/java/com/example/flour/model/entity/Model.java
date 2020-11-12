package com.example.flour.model.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@NoArgsConstructor
@AllArgsConstructor
@Data
@Entity
@ToString(exclude = {"engineer", "modelDetailList"})
public class Model {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String version;

    private String content;

    private Integer price;

    private LocalDateTime registeredAt;

    private LocalDateTime unregisteredAt;

    private LocalDateTime updatedAt;

    private String updatedBy;

    @ManyToOne
    private Engineer engineer;

    @OneToMany(fetch = FetchType.LAZY, mappedBy = "model")
    private List<ModelDetail> modelDetailList;

}
