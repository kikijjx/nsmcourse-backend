from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.experiment import Experiment
from app.schemas.experiment import ExperimentCreateUpdate, ExperimentResponse
from datetime import datetime

experiment_router = APIRouter()

@experiment_router.get("/experiments")
def get_experiments(db: Session = Depends(get_db)):
    experiments = db.query(Experiment).all()
    if not experiments:
        raise HTTPException(status_code=404, detail="Experiments not found")
    return experiments


@experiment_router.post("/experiments", response_model=ExperimentResponse)
def create_experiment(experiment: ExperimentCreateUpdate, db: Session = Depends(get_db)):
    db_experiment = Experiment(
        theme_id=experiment.theme_id,
        title=experiment.title,
        description=experiment.description,
        parameters=experiment.parameters,
        updated_at=datetime.utcnow(),
    )
    db.add(db_experiment)
    db.commit()
    db.refresh(db_experiment)
    return db_experiment


@experiment_router.put("/experiments/{experiment_id}", response_model=ExperimentResponse)
def update_experiment(experiment_id: int, experiment: ExperimentCreateUpdate, db: Session = Depends(get_db)):
    db_experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not db_experiment:
        raise HTTPException(status_code=404, detail="Experiment not found")
    
    db_experiment.theme_id = experiment.theme_id
    db_experiment.title = experiment.title
    db_experiment.description = experiment.description
    db_experiment.parameters = experiment.parameters
    db_experiment.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_experiment)
    return db_experiment

@experiment_router.delete("/experiments/{experiment_id}", response_model=dict)
def delete_experiment(experiment_id: int, db: Session = Depends(get_db)):
    db_experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not db_experiment:
        raise HTTPException(status_code=404, detail="Experiment not found")
    
    db.delete(db_experiment)
    db.commit()
    return {"detail": "Experiment deleted successfully"}


@experiment_router.get("/experiments/{experiment_id}", response_model=ExperimentResponse)
def get_experiment(experiment_id: int, db: Session = Depends(get_db)):
    db_experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not db_experiment:
        raise HTTPException(status_code=404, detail="Experiment not found")
    return db_experiment
