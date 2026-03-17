#!/usr/bin/env python3
"""
Pancake Monitor Template (Commercial)
Bản mẫu sạch để thương mại hóa.
Không chứa token thật, page id thật hoặc dữ liệu khách hàng thật.
"""

from datetime import datetime, timedelta, timezone

VN_TZ = timezone(timedelta(hours=7))
UTC_TZ = timezone.utc


def parse_dt(value: str):
    if not value:
        return None
    raw = value.strip()
    if raw.endswith('Z'):
        dt = datetime.fromisoformat(raw.replace('Z', '+00:00'))
    else:
        dt = datetime.fromisoformat(raw)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=UTC_TZ)
    return dt.astimezone(VN_TZ)


def next_stage(wait_minutes: int) -> int:
    if wait_minutes >= 60:
        return 3
    if wait_minutes >= 40:
        return 2
    if wait_minutes >= 20:
        return 1
    return 0


def actual_stage(wait_minutes: int, last_notified_stage: int) -> int:
    desired = next_stage(wait_minutes)
    return min(desired, last_notified_stage + 1)


def should_ignore_as_noise(text: str) -> bool:
    if not text:
        return True
    noise_patterns = {
        'xin chào', 'dạ', 'ok', 'vâng', 'thanks', 'thank you'
    }
    return text.strip().lower() in noise_patterns


def handoff_rule_summary() -> str:
    return (
        'Khi đến lần nhắc 3: remove tag sale cũ, add 2 tag sale còn lại, '
        'chỉ coi là handoff thành công nếu cả remove và add đều thành công.'
    )


if __name__ == '__main__':
    sample = '2026-03-10T07:02:16.000000'
    print('sample raw:', sample)
    print('sample vn:', parse_dt(sample).isoformat())
    print('stage demo:', actual_stage(75, 0))
