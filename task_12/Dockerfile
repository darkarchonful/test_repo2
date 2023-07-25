FROM python
RUN touch test_run.py
COPY entry.py cmd.py ./
#RUN python -m pip install --upgrade pip
#CMD python cmd.py
ENTRYPOINT python entry.py

FROM ubuntu
