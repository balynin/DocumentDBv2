#!/bin/bash
celery --app tasks:app worker -l INFO