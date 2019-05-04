package {{group_id}}.{{artifact_id_periods}}.repository;

import {{group_id}}.{{artifact_id_periods}}.entity.{{artifact_id_capitalized}}Entity;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface {{artifact_id_capitalized}}Repository extends JpaRepository<{{artifact_id_capitalized}}Entity, UUID> {

}
