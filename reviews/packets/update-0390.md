<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0390.txt",
      "sha256": "a1bcaccbd2507329f2a526bef5f113e1f7f4f7fa26590954f27528428a261900",
      "bytes": 13695
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8657a79cf17ce9aa96d9f6303c04acac894ec90be484acab131d7214f2aa3666",
      "bytes": 5434
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "05d47b17fbcfd6819ae22361ddd5fa3da687ab9df4b274b4abac295376ae8afb",
      "bytes": 13511
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c3e5589068e75ab14b10282575bf1a2a27450fc4e97c430476ce6419a9229c97",
      "bytes": 23802
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "95c58450159384d13ba587afcda8fbc9100fe861f9898ed6ae8afc410c11924a",
      "bytes": 10457
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 15671
}
-->

# Durable State Update — Chapter 390

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 390. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 390. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 390,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 390,
    "continuity_sources": [390],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Taekyung is a Supreme Peak martial artist who has crossed the wall; his exact current level, Fame, complete Titles, martial-art stages, and unassigned points remain unstated.",
    "Taekyung has returned to the modern world and is working with Chinese authorities to stop the monster disaster while seeking Lei Fei and the missing Sichuan Hunters.",
    "Sichuan Province remains in a wartime state after the monster wave began in Gaoping District, Nanchong City.",
    "China has declared martial law, and UN-approved peacekeeping forces have joined the front.",
    "Wei Penghu is a Senior General and Minister of Defense at the Central Military Commission; he raised his missing nephew Lei Fei as his own son.",
    "Xiao Yang is Chairman of the Central Military Commission, General Secretary, and state chairman of the People's Republic of China, and retains full authority over the crisis response.",
    "Team Leader Choi trusts Taekyung, was rescued by him from a drinking-game predicament, and agreed to adjust Taekyung's settlement share to nine-to-one.",
    "The six S-rank Hunters were assigned to six fronts; Prince Felix left before dawn after receiving a battle signal.",
    "Magic Johnson is an S-rank Hunter, one of three Archmages worldwide, and a combat-specialized War Mage.",
    "Pai Chen is an S-rank Hunter, Great Cataclysm hero, and former romance-film actress who appears much younger than her actual age.",
    "Wu Heixing is an S-rank Hunter from a powerful Chinese Communist Party family; he is arrogant, volatile, status-conscious, and regards the missing Lei Fei as an insurmountable rival.",
    "Prince Felix Alexander Louis is a British prince, third in line to the throne, and holds multiple senior British titles; William serves as his formal attendant.",
    "The Sichuan Tang Clan was devastated by Dark Heaven, owes Taekyung's group a debt, and is considering relocation.",
    "The Chengdu International Airport attack involved an undead army controlled by three incomplete Arch Liches, all of whom Taekyung destroyed.",
    "The Skeleton Warlord absorbed the death energy of the remaining two Arch Liches and became much stronger, but the persistence and full extent of that increase remain unknown.",
    "Dark Heaven's agents, purpose, and connection to the hidden transport formation remain unresolved.",
    "Lee Jungryong is the practical leader of Ares Guild and one of the world's top three S-rank Hunters; he recognizes Choi Minwoo's growth and that Jin Taekyung has crossed the wall.",
    "Wu Heixing used Sound Transmission and possesses martial-arts knowledge; Taekyung defeated him after he attacked, taking his Supreme Potion and leaving him with an Advanced Potion.",
    "An unrefusable Unexpected Quest, The Battle Situation Has Become Critical, orders Taekyung to reach the battlefield quickly and defeat the enemies.",
    "The monster army has exceeded 100,000, and the western front has been breached by a rapid monster advance while Jin Taekyung's force remains engaged."
  ],
  "continuity_sources": [
    389
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved.",
    "Dark Heaven's larger purpose, its reason for sparing Taekyung, and the origin and function of the hidden transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination, along with the timing and outcome of the Samgoe escort to Henan, remain unresolved.",
    "The request Dongbong wants to make of Taekyung, Mungyeong's eventual response to the coming war, and the identity and fate of the boy from the Chengdu port remain unresolved.",
    "Ae-hyang's superior and the consequences of the Sichuan Governor's false memorial remain unresolved.",
    "The relationship between the Lich and the Arch Lich, the full extent of the Skeleton Warlord's increased power, and the monster wave's larger plan remain unresolved.",
    "Lei Fei's fate and the fate of the missing Sichuan Hunters remain unresolved.",
    "The subject and consequences of Lee Jungryong's discussion with Wu Heixing, Wu Heixing's reason for sending the Sound Transmission, and the outcome of the western-front battle remain unresolved."
  ],
  "safe_through": 389,
  "temporary_decisions": [
    "Render Zhonghua as Zhonghua and preserve the Jongseok mishearing joke for 총서기.",
    "Render Xiao Yang's offices as Chairman of the Central Military Commission, General Secretary, and state chairman.",
    "Render 대마법사 as Archmage and 워 메이지 as War Mage.",
    "Retain Teacher Jin for 진 선생 and Comrade Chairman for 주석 동지.",
    "Render 반도의 빵즈 as peninsula bangzi and retain the derogatory-slur footnote.",
    "Preserve Taekyung's conversational, self-mocking first-person voice and the source's jokes, including the forum's exaggerated online register.",
    "Render established names and titles consistently, including Pai Chen, Wu Heixing, Prince Felix Alexander Louis, William, Senior General Liao, the Princelings, the Shanghai clique, Sound Transmission, Sword Force, Advanced Potion, and Supreme Potion.",
    "Render 다급해진 전황 as The Battle Situation Has Become Critical, 유엔 안전보장이사회 as United Nations Security Council, 형님 as hyung-nim for Shao Shen's address to Jin, and 정 드래곤 as Jung Dragon."
  ],
  "version": 1
}
```

## Expedition bridge dossier

# Expedition Seed Dossier

This dossier is intentionally conservative. It orients the Chapter 370 catch-up.
It is not a substitute for translating Chapters 66–369, and it must not leak
plot from parked Chapters 371–375.

## Hard boundary

- Accepted English continuity is reliable through Chapter 65.
- Chapters 66–369 are skipped and have no accepted local English in this
  expedition.
- Chapter 370 is the next chapter to translate. Its Korean source is the
  authority for every beat in that chapter.
- Parked accepted translations of Chapters 374–375 exist in this branch. Do not
  read them, their reviews, or old 371–373 bridge summaries while drafting
  370–373.
- When the Korean source of the current chapter conflicts with this dossier or
  with Chapter 65 continuity, the current source wins. Do not invent missing
  backstory; preserve ambiguity and flag an unresolved continuity issue.

## Opening position for Chapter 370

Chapter 370's source opens at the Sichuan Tang Clan. About seven days have
passed since the Three-Sect Bloodbath. The clan's gates, long closed, are open
to reconstruction and to orthodox guests. Do not assert later names, ranks,
quests, or outcomes that the current chapter has not yet shown.

## Translation guardrails

- Treat the Korean source as authoritative for every line of the chapter being
  translated.
- Do not back-project titles, names, ranks, or skills from parked later
  chapters or web searches into the skipped range without current-source
  evidence.
- Use established local terminology where it exists from Chapters 0–65.
- For terms first evidenced in the current source, follow the ledger and
  first-use rules. Record new bindings through the normal update stage.
- The light, self-mocking first-person voice and the source's jokes remain
  important, but missing continuity must never be filled by invented exposition.

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 독룡각 | **Poison Dragon Pavilion** | Pavilion led by Tang Horyong |
| 당호룡 | **Tang Horyong** | Acting Family Head of the Sichuan Tang Clan |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok |
| 당사독 | **Tang Sadok** | Poison King and Family Head of the Sichuan Tang Clan |
| 경천신니 | **Heaven-Shaking Divine Nun** | Murder victim named alongside Tang Sadok |
| 삼문혈사 | **Three-Sect Bloodbath** | Recent attack on three major orthodox sects |
| 삼괴 | **Samgoe** | Principal culprit being escorted to Henan |
| 구파일방 | **Nine Sects and One Gang** | Major orthodox organizations |
| 오대세가 | **Five Great Families** | Major orthodox families |
| 소림혈사 | **Shaolin Bloodbath** | Earlier attack that galvanized orthodox Murim |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 만독지환 | **Myriad Poison Ring** | Item Taekyung considers taking before departure |
| 미미 | **Mimi** | Tang Sadok's snake and longtime companion; temporarily entrusted to Cheongpung. |
| 동봉 | **Dongbong** | Name or designation associated with the Divine Physician. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 백염 | **White Flame** | Previously bound item listed by the System. |
| 사죄와 용서 | **Atonement and Forgiveness** | Hidden Quest completed by Taekyung. |
| 당문의 은인 | **Benefactor of the Tang Clan** | Title acquired by Taekyung. |
| 아미파 | **Emei Sect** | Orthodox sect whose nuns conduct the funeral rites. |
| 청성파 | **Qingcheng Sect** | Orthodox sect represented among the assisting martial artists. |
| 개방 | **Beggars' Sect** | Organization represented by the attending beggars. |
| 묘령사태 | **Satae Myo Ryeong** | Middle-aged Emei nun overseeing the funeral prayers. |
| 명진 | **Myeongjin** | Daoist assisting with the funeral rites. |
| 궁기방 | **Gung Gibang** | Young beggar and Future Beggar Chief. |
| 후개 | **Future Beggar Chief** | Title used for Gung Gibang. |
| 기련삼괴 | **Qilian Samgoe** | The trio of monsters that includes Samgoe and Ilgoe. |
| 일괴 | **Ilgoe** | The strongest of the Qilian Samgoe, defeated single-handedly by Jin Taekyung. |
| 칠선자 | **Chilseonja** | Mysterious martial artist who blocked Samgoe's attack and saved Hyuk Mujin. |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 화산신룡 | **Huashan Divine Dragon** | Epithet used for Jin Taekyung. |
| 열화신룡 | **Blazing Fire Divine Dragon** | New epithet acquired by Jin Taekyung. |
| 청풍고검 | **Clear Wind Ancient Sword** | Sect Leader of the Qingcheng Sect; epithet of the old Daoist. |
| 멸절신니 | **Extinction Divine Nun** | New Sect Leader of the Emei Sect after the death of the Heaven-Shaking Divine Nun. |
| 천주 | **Heavenly Lord** | Being worshiped as a god by Dark Heaven's fanatics. |
| 혈주 | **Blood Lord** | Dark Heaven figure whose power and abilities are recalled by Jin Taekyung. |
| 열화동 | **Blazing Fire Cave** | Cave at Mount Jiuhua containing an advanced arcane formation. |
| 진성애 | **Jin Seong-ae** | Jin Taekyung's joking title for himself as a sex-education teacher. |
| 구성애 | **Gu Seong-ae** | Real-world sex-education teacher referenced in Jin Taekyung's joke. |
| 삼도천 계곡 | **Valley of the Sanzu River** | Valley named after the Buddhist river separating the living world from the afterlife. |
| 노군백 | **No Gunbaek** | Level 170 opponent named in a System defeat message. |
| 귀염미 | **Gwiyeommi** | Pen name of a romance novelist. |
| 홍무 | **Hongwu** | Era name beginning when the civil war ends and a new emperor ascends. |
| 성도 | **Chengdu** | City whose western port is the departure point. |
| 선화아 | **boatman** | Nautical title used for Mu Song. |
| 무송 | **Mu Song** | Bronze-skinned boatman associated with the water bandits. |
| 애향 | **Ae-hyang** | The Sichuan Governor's favorite concubine; covertly manipulative. |
| 상산왕 | **King of Shangshan** | Noble whose token was carried by Taekyung's group. |
| 수룡채 | **Water Dragon Stronghold** | Stronghold whose flag flies from the ships carrying Taekyung's group. |
| 흑룡갑 | **Black Dragon Armor** | The armor's former name; only a fragment survives. |
| 화룡갑 | **Flame Dragon Armor** | New name Taekyung gives the bound armor fragment. |
| 열화신공 | **Blazing Flame Divine Art** | Art whose formula Taekyung uses to infuse the armor. |
| 삼공 | **Grand Councilor** | High office referenced in the Sichuan Governor's ambitions. |
| 최 팀장 | **Team Leader Choi** | Taekyung's modern-world team leader aboard the private jet. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 스켈레톤 워로드 | **Skeleton Warlord** | Undead commander accompanying Taekyung's group. |
| 샤오 양 | **Xiao Yang** | Chairman credited by passengers with making a special request for Taekyung. |
| 중국 중앙위원회 | **Central Committee of China** | Organization that sent the private jet. |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |
| 청두 국제공항 | **Chengdu International Airport** | Destination airport under attack. |
| 헌터 마켓 | **Hunter Market** | Market where Taekyung bought the spear at a discount. |
| 검은 별 | **Black Star** | Epithet of the exceptionally powerful lead wyvern. |
| 샤오 쉔 | **Shao Shen** | Twenty-year-old spear-wielding Hunter of the Public Security Armed Forces. |
| 야오위 | **Yao Wei** | A-rank Hunter, Shao Shen's friend and comrade. |
| 류인친 | **Ryu Inchin** | Named combatant of the Public Security Armed Forces; exact relationship to the person calling him hyung is unresolved. |
| 공안 무력부 | **Public Security Armed Forces** | Chinese Hunter organization. |
| 인민 해방군 | **People's Liberation Army** | Chinese military force stationed at the airport. |
| 중화인민공화국 | **People's Republic of China** | Country whose flag appears on Shao Shen's armor. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 오성홍기 | **Five-Star Red Flag** | National flag of the People's Republic of China. |
| 듀라한 | **Dullahan** | Higher undead monster form taken by Yao Wei. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |
| 중앙 군사 위원회 | **Central Military Commission** | Chinese military body Shao Shen assumes dispatched the unknown S-rank Hunter. |
| 화염신장 | **Flame Divine Palm** | Named fire-based palm technique used by Taekyung. |
| 멸염신권 | **Flame-Annihilating Divine Fist** | Named fire-based fist technique used by Taekyung. |
| 염화일로 | **Flamefire Path** | Named fire-based movement technique used by Jin Taekyung. |
| 아크 리치 | **Arch Lich** | Superior undead being referenced by the three incomplete Liches. |
| 스켈레톤 메이지 | **Skeleton Mage** | Undead unit the three beings consider deploying. |
| 데스나이트 | **Death Knight** | Powerful undead being the three beings plan but fail to create. |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 언데드 헌터 | **Undead Hunter** | Title acquired by Jin Taekyung as the Unexpected Assault Quest Reward. |
| 죽음의 강 | **River of Death** | River upon which the undead swear binding oaths. |
| 검은 숲 | **Black Forest** | Domain the Skeleton Warlord claims to rule. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |
| 상장 | **Senior General** | Wei Penghu's military rank, explained as four-star. |
| 오르페우스 폰 막시무스 발렌시아 바이엘른 | **Orpheus von Maximus Valencia Bayern** | Self-styled name used by one of the three undead beings; retains the source's humorous wordplay. |
| 레이페이 | **Lei Fei** | Previously undisclosed Chinese S-rank Hunter and commander of the Sichuan Public Security Armed Forces; missing with his Hunters. |
| 난충시 | **Nanchong City** | City containing Gaoping District, where the monster wave began. |
| 가오핑구 | **Gaoping District** | District in Nanchong City where the first monster-wave signs appeared. |
| 청성산 | **Mount Qingcheng** | Mountain containing the temporary operations headquarters. |
| 핑핑이 | **Pingping** | Taekyung's joking guess at the name of the deceased former chairman; not established as the actual name. |
| 팽팽이 | **Pengpeng** | Taekyung's joking alternative guess at the name of the deceased former chairman; not established as the actual name. |
| 매직 존슨 | **Magic Johnson** | S-rank Hunter, one of the three Archmages, and a combat-specialized War Mage. |
| 대마법사 | **Archmage** | Title held by only three people worldwide. |
| 워 메이지 | **War Mage** | Magic Johnson's combat-specialized Archmage title. |
| 총서기 | **General Secretary** | One of Xiao Yang's offices. |
| 국가 주석 | **state chairman** | Xiao Yang's office as leader of the People's Republic of China. |
| 중앙군사위원회 | **Central Military Commission** | Commission chaired by Xiao Yang. |
| 중국 공산당 | **Chinese Communist Party** | Party whose Central Military Commission Xiao Yang chairs. |
| 종석이 | **Jongseok** | Taekyung's mistaken personal-name joke for the General Secretary; not the chairman's actual name. |
| 파이 첸 | **Pai Chen** | S-rank Hunter, Great Cataclysm hero, and former romance-film actress. |
| 우헤이싱 | **Wu Heixing** | S-rank Hunter antagonistic toward Taekyung. |
| 윌리엄 | **William** | Prince Felix's formal attendant. |
| 필릭스 알렉산더 루이 | **Prince Felix Alexander Louis** | British prince and third in line to the throne. |
| 케임브리지 공작 | **Duke of Cambridge** | Title held by Prince Felix. |
| 스트래선 백작 | **Earl of Strathearn** | Title held by Prince Felix. |
| 캐릭퍼거스 남작 | **Baron Carrickfergus** | Title held by Prince Felix. |
| 가터 훈장의 기사 | **Knight of the Garter** | Honor held by Prince Felix. |
| 시슬 훈장의 기사 | **Knight of the Thistle** | Honor held by Prince Felix. |
| 아레스 길드 | **Ares Guild** | Powerful Guild whose practical leader is Lee Jungryong. |
| 랴오 상장 | **Senior General Liao** | Chinese Senior General and member of the Princelings faction. |
| 태자당 | **Princelings** | The Communist Party's largest faction; Liao belongs to it. |
| 상하이방 | **Shanghai clique** | Faction associated with Xiao Yang and Wei Penghu. |
| 천안문 광장 | **Tiananmen Square** | Place referenced in Taekyung's hypothetical beheading joke. |
| 북경 | **Beijing** | Possible destination for teleported nuclear warheads. |
| 다급해진 전황 | **The Battle Situation Has Become Critical** | Name of the unrefusable Unexpected Quest generated aboard the departing jet. |
| 유엔 안전보장이사회 | **United Nations Security Council** | International body whose fifteen national leaders join Xiao Yang's emergency meeting. |
| 정 드래곤 | **Jung Dragon** | Public nickname for Lee Jungryong. |
| 김철수 | **Kim Cheol Soo** | Generic Korean name used in a forum joke. |
| 제임스 | **James** | Generic English name used in a forum joke. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 혁무진 | 궁기방 | orthodox_ally_to_orthodox_ally | Young Hero Gung | blunt-but-formal | Uses 궁 소협 while teasing Gung Gibang about his injuries. |
| 혁무진 | 청풍 | junior_ally_to_younger_ally | Young Hero Cheong | formal-but-bewildered | Uses 청 소협 when reacting to Cheongpung's warning. |
| 혁무진 | 진태경 | subordinate_to_squad_leader | Squad Leader | deferential | Calls Taekyung 조장님 when announcing his awakening. |
| 궁기방 | 진태경 | squadmate_to_squad_leader | Jin Taekyung | familiar-but-direct | Calls Taekyung by name when he wakes. |
| 진태경 | 청풍고검 | junior_to_elder_sect_leader | Perfected One | respectful-formal | Uses 진인 when greeting the Qingcheng Sect Leader. |
| 청풍고검 | 진태경 | elder_sect_leader_to_junior_ally | Fellow Daoist Jin | respectful-but-familiar | Uses 진 도우 when greeting Taekyung. |
| 멸절신니 | 진태경 | elder_sect_leader_to_benefactor | Benefactor Jin | respectful-formal | Uses 진 시주 when greeting Taekyung. |
| 멸절신니 | 적천강 | orthodox_elder_to_orthodox_elder | Benefactor Jeok | respectful-but-familiar | Uses 시주 when responding to Jeok Cheongang. |
| 진태경 | 적천강 | disciple_to_elder_master | Old Man | casual-but-affectionate | Uses 노야 while thanking Jeok Cheongang. |
| 적천강 | 문경 | orthodox_elder_to_younger_orthodox_elder | Wen | hostile-but-blunt | Jeok Cheongang addresses Mungyeong as 문가 while intervening on Taekyung's behalf. |
| 진태경 | 문경 | ally_to_secret_identity_holder | Mungyeong | casual-but-teasing | Taekyung accepts the requested name and deliberately uses it in a familiar vocative. |
| 동봉 | 문경 | disciple_to_master | Master | deferential | Dongbong repeatedly addresses Mungyeong as 스승님 after affirming his identity as the Divine Physician. |
| 무송 | 진태경 | older_ally_to_junior_ally | junior | deferential-but-uncertain | Mu Song switches from junior to Young Hero Jin and Great Hero before Taekyung tells him to use junior. |
| 사천성주 | 애향 | lover_to_favorite_concubine | Ae-hyang | intimate-affectionate | The Sichuan Governor repeatedly calls his favorite concubine by name and speaks to her in an indulgent intimate manner. |
| 애향 | 사천성주 | favorite_concubine_to_lover | my dear | intimate-coquettish | Ae-hyang addresses the Sichuan Governor as 가가 while flattering and manipulating him. |
| 진태경 | 최 팀장 | subordinate_to_team_leader | Team Leader | polite-but-direct | Taekyung uses 팀장님 while asking Choi for help and addressing him during the crisis. |
| 최 팀장 | 진태경 | team_leader_to_trusted_hunter | Mr. Jin Taekyung | professional-deferential | Choi repeatedly uses 진태경 씨 while relying on Taekyung to resolve the attack. |
| 진태경 | 기장 | passenger_to_captain | Captain | casual-urgent | Taekyung directly asks the captain for permission before cutting open the aircraft door. |
| 샤오 쉔 | 진태경 | foreign_hunter_to_recognized_hero | Teacher Jin | formal-polite | Uses 진 선생님 after recognizing Taekyung as Sibeol-jwa. |
| 스켈레톤 워로드 | 진태경 | undead_subordinate_to_human_controller | vile human | hostile-but-familiar | Recurring address used while speaking to Taekyung during the battle. |
| 진태경 | 스켈레톤 워로드 | human_controller_to_undead_subordinate | Boney | casual-teasing | Taekyung uses Boney as a deliberately demeaning pet nickname. |
| 웨이펑후 | 진태경 | senior_military_official_to_foreign_hero | Teacher Jin | respectful-formal | Wei Penghu uses 진 선생 when introducing himself and inviting Taekyung to the operations headquarters. |
| 조종사 | 웨이펑후 | pilot_to_senior_military_official | Comrade Minister of Defense | deferential-formal | Pilot's formal greeting on Wei Penghu's arrival. |
| 웨이펑후 | 샤오 쉔 | senior_military_official_to_subordinate_hunter | Senior Colonel Shao Shen | respectful-but-familiar | Wei Penghu uses Shao Shen's rank and name when bidding him farewell. |
| 샤오 쉔 | 웨이펑후 | subordinate_hunter_to_senior_military_official | Comrade Minister of Defense | deferential-formal | Shao Shen promises to complete his mission and rejoin Wei Penghu. |
| 샤오 양 | 진태경 | head_of_state_to_foreign_hunter | Teacher Jin | respectful-formal | Xiao Yang uses 진 선생 when greeting and addressing Taekyung. |
| 샤오 양 | 웨이펑후 | head_of_state_to_old_friend_and_subordinate | Minister of Defense Wei Penghu | authoritative-but-familiar | Xiao Yang addresses Wei by office and name while discussing authority over the Central Military Commission. |
| 웨이펑후 | 샤오 양 | subordinate_to_head_of_state | Comrade Chairman | deferential-formal | Wei uses 주석 동지 when responding to Xiao Yang. |
| 진태경 | 파이 첸 | junior_to_older_senior | Ms. Chen / Chen | polite-but-familiar | Taekyung initially uses Ms. Pai Chen; she permits Chen or older sister, but he rejects the latter after learning her age. |
| 우헤이싱 | 진태경 | hostile_peer | peninsula bangzi | abusive-hostile | Wu Heixing repeatedly addresses Taekyung with an anti-Korean slur. |
| 진태경 | 우헤이싱 | hostile_peer | mainland chink | abusive-hostile | Taekyung answers Wu Heixing's slur with an explicit anti-mainland insult. |
| 윌리엄 | 필릭스 알렉산더 루이 | attendant_to_royal_prince | His Royal Highness Prince Felix | deferential-ceremonial | William recites Felix's complete royal titles when instructing the room to show respect. |
| 필릭스 알렉산더 루이 | 윌리엄 | royal_prince_to_attendant | William | commanding-familiar | Felix stops William's repeated title recital by name. |
| 매직 존슨 | 이정룡 | senior_s_rank_hunter_to_peer | Lee | casual-flirtatious | Greets Lee Jungryong familiarly and jokes about confessing his love. |
| 이정룡 | 매직 존슨 | peer_s_rank_hunter | Magic Johnson | casual-but-respectful | Responds to Magic Johnson's flirtatious greeting. |
| 파이 첸 | 이정룡 | peer_s_rank_hunter | Mr. Lee | playful-polite | Responds to Lee's romantic joke with teasing politeness. |
| 우헤이싱 | 이정룡 | junior_s_rank_hunter_to_top_s_rank_hunter | Mr. Lee | intimidated-deferential | Uses 이 선생님 and suppresses his usual hostility in Lee's presence. |
| 필릭스 알렉산더 루이 | 이정룡 | royal_prince_to_top_s_rank_hunter | Jungryong Lee | formal-polite | Addresses Lee through the translation device without the expected royal honorific. |
| 이정룡 | 필릭스 알렉산더 루이 | top_s_rank_hunter_to_royal_prince | that prince | casual-dismissive | Does not use the prince's formal title. |
| 웨이펑후 | 이정룡 | senior_military_official_to_top_s_rank_hunter | Mr. Lee | respectful-formal | Addresses Lee as 이 선생 during the meeting. |
| 랴오 상장 | 웨이펑후 | senior_general_to_minister_of_defense | Comrade Minister of Defense | blunt-but-formal | Challenges Wei Penghu's strategy while invoking factional rivalry. |
| 웨이펑후 | 랴오 상장 | minister_of_defense_to_senior_general | Senior General Liao | formal-authoritative | Invites Liao to speak and later rebukes his nuclear proposal. |
| 파이 첸 | 매직 존슨 | peer_s_rank_hunter_to_peer_s_rank_hunter | Johnson | casual-but-familiar | Uses his surname while inviting him to drink. |
| 매직 존슨 | 파이 첸 | peer_s_rank_hunter_to_peer_s_rank_hunter | Miss Chen | casual-polite | Uses a polite English honorific while inviting her to join the group. |
| 파이 첸 | 최 팀장 | senior_s_rank_hunter_to_trusted_ally | handsome bachelor | playful-familiar | Playful address while recruiting Team Leader Choi for the drinking party. |
| 매직 존슨 | 최 팀장 | peer_ally_to_team_leader | Choi | casual-teasing | Magic Johnson repeatedly addresses Team Leader Choi by surname while joking with him. |
| 파이 첸 | 진태경 | senior_s_rank_hunter_to_younger_ally | young man | familiar-but-caring | Pai Chen uses a familiar senior-to-junior address while advising Taekyung before deployment. |
| 진태경 | 아저씨 | passenger_to_pilot | Sir | casual-urgent | Taekyung addresses the pilot informally while demanding full throttle. |
| 샤오 쉔 | 진태경 | subordinate_hunter_to_foreign_hero | hyung-nim | deferential-but-familiar | After Jin permits the familiar title, Shao Shen stammers out hyung-nim while addressing him before his troops. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 퀘스트              | **Quest**                      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 상장 | **Senior General** | Wei Penghu's military rank, explained as four-star. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 389
- **Aliases:** Sleeping Dragon of Shanxi; Huashan Divine Dragon; Blazing Fire Divine Dragon
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; Supreme Peak martial artist who has crossed the wall; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃390화



촤아아악!

강기가 스쳐 지나간 자리, 솟구치는 목들과 함께 뜨거운 핏물이 뿜어져 나온다.

나는 볏짚처럼 쓰러지는 오우거의 몸뚱이를 밟고 높이 솟아올랐다. 목덜미에 닿는 햇볕이 따스하다.

‘거, 싸우기 딱 좋은 날씨네.’

때는 정오. 장소는 나무 한 그루 없는 황무지.

운집해 있는 천여 마리의 몬스터들 한가운데에 태양을 등진 내 그림자가 비친다.

급강하와 동시에 내리그어지는 창날의 움직임까지도.

‘천격(天格).’

콰아아아앙!

화룡의 발톱이 지상을 할퀴었다.

하늘이 쪼개지는 듯한 굉음. 지면이 수 미터 깊이로 주저앉고 흙과 돌 부스러기가 사방으로 비산한다.

전장의 중심에서 일어난 열풍(熱風)의 회오리가 칼날이 되어 몬스터들을 휩쓸었다.

콰아아아!

띠링. 띠링. 띠링…….

흙먼지로 인해 뿌옇게 물든 시야 속, 몬스터 처치를 알리는 시스템 알림과 함께 녹색 핏물이 투두둑 쏟아진다.

가볍게 손을 내젓자 먼지구름이 흩어지고 멍한 얼굴로 나를 응시하는 몬스터들이 보였다.

- 취릭?

- 크륵?

도대체 이게 무슨 상황인지 모르겠다는 듯한 눈빛들. 깊게 숨을 들이쉰 나는 공력을 실은 외침을 토해 냈다.

“쓸어-!”

그리고 다음 순간.

「와아아아아아!」

귀가 먹먹해지는 함성과 함께, 어느새 들이닥친 천여 명의 헌터들이 파도처럼 몬스터 군단을 덮쳤다.

콰드드드득!

퍼버벅!

속수무책으로 허물어지는 몬스터들을 보며 한 가지 확신이 들었다.

‘이 전투, 이겼다.’

농사가 끝났으니 이제 추수를 해야 할 때.

나는 보스 몬스터로 보이는 트윈 헤드 오우거를 향해 걸음을 옮겼다.

내 금쪽같은 경험치. 아니, 아군의 피해를 최소화하기 위해서였다.

「저놈이 우두머리다! 원거리 부대!」

“야, 야! 손 떼! 내가 처리할 테니까 털끝 하나 건드리지 마!”

하늘에 맹세컨대, 정말 요만큼의 사심도 없다.

“…….”

음, 곰곰이 생각해 보니까 맹세할 필요까지는 없을 것 같다.

- 간악한 인간이여. 부산물을 차지하려는 네 속셈이 뻔히 들여다보인다. 내 군단을 학살할 때도 탐욕을 숨기지 않았지!

“닥치고 네 할 일이나 하지? 빨리 언데드로 동족상잔 시작해.”

- 안 그래도 그러려고 했다. 자라나라 해골해…… 어?

“왜 그래?”

- 왜 내 힘이 통하지 않는 거지? 혹시 버그인가?

“……그런 단어는 또 어디서 주워들은 거야.”

점점 현대화가 진행 중인 스켈레톤 워로드가 낙담한 목소리로 말했다.

- 안으로 들어올수록 아크 리치의 지배력이 강해지는 것 같다. 아아, 군단 없는 사령관이라니. 실로 통탄을 금치 못하겠구나. 이래서야 죽은 것이나 다름없어!

“…….”

이 새끼는 본인을 뭐라고 생각하는 거지.

이제는 이미 죽어 있다고 말해 주는 것도 지겹다. 나는 내심 한숨을 내쉬며 우두머리를 향해 달려들었다.



* * *



「대승입니다! 이번에도 대승이에요!」

샤오 쉔이 발갛게 달아오른 얼굴로 외쳤다. 지금까지 열 번도 넘게 본 광경이라 이제는 나와 최 팀장도 그러려니 하고 넘기는 분위기다.

‘뭐, 신날 만도 하지.’

자그마치 천여 마리의 몬스터 대군을 전멸시키기까지 겨우 두 시간 남짓.

그것도 단 한 사람의 사망자도 없이 마무리 지었으니 기념비적인 승리인 것은 맞다. 이런 상황에서는 오히려 덤덤한 것이 이상한 거지.

「저희 쪽 피해는 중상자 스물셋, 경상자 서른 명이 전부입니다. 아, 이건 정말……!」

오줌 마려운 강아지처럼 몸을 부르르 떤 샤오 쉔이 반짝거리는 눈동자로 나를 바라봤다.

「어떻게 매번 이럴 수 있는 겁니까?」

“음. 그건 내가 강하기 때문이 아닐까.”

내 대답에 최 팀장이 살짝 어이없다는 눈빛을 보냈다.

“왜요?”

“아니. 보통 이럴 때는 운이 좋다거나, 뭐 그런 겸양의 말을 하지 않습니까?”

“보통은 그렇죠. 근데 운이 좋은 게 아니라 정말 강해서 이런 걸 어떡합니까. 안 그러냐, 쉔?”

샤오 쉔이 엄청난 속도로 고개를 끄덕였다.

「맞습니다! 형님은 최고십니다!」

“녀석. 훌륭한 아부의 표본이로구나.”

“…….”

주거니 받거니 하는 우리의 모습에 최 팀장이 고개를 절레절레 저었다.

“뭐요.”

“아닙니다. 하긴, 이래야 진태경 씨답긴 하죠.”

뭐지, 묘하게 기분 나쁘게 들리는데.

어깨를 으쓱한 나는 샤오 쉔을 향해 물었다.

“그보다 본부 쪽은?”

「아, 그렇지 않아도 전투 시작 전에 연락을 취했습니다.」

연락을 취했다는 건, 휘하에 있는 헌터 몇 명을 미리 보내 놨다는 뜻이다.

요즘 같은 세상에 전령(傳令)이 웬 말이냐 싶겠지만, 어쩔 수 없다. 마법으로 통신과 위성 감시가 불가능한 상황이니 죽어라 뛰거나 차량을 이용하는 수밖에.

그래도 조명탄을 포함한 여러 문물이 있으니 다행이다.

“또 한참 걸리겠군.”

「뒤따라오는 중이었으니 그리 오래 걸리지는 않을 겁니다.」

“피곤하겠지만 천막이라도 쳐서 애들 쉬게 해. 금방 끝나긴 했어도 전투 끝나면 진이 쏙 빠진다.”

「대형 몬스터 정도는 우리 쪽에서 처리해 놔야 하지 않을까요? 아무래도 본부가 옮기기에는 힘들 것 같아서…….」

“그것도 맞는 말이긴 하지.”

본부란 우리와 함께 움직이는 군 병력을 말한다.

나를 포함한 공안 무력부 소속 헌터들이 선봉에서 몬스터를 무찌르면, 뒤따라온 군 병력이 해당 지역과 몬스터 사체들을 ‘청소’하는 방식이었다.

굳이 청소라고 표현하는 이유는 그 목적이 부산물 노획이 아니기 때문이다.

이건 말 그대로 청소다. 내가 맡은 서부 전선의 군대는 죽은 몬스터들이 언데드로 부활할 수 없도록 사체를 토막 내고, 후방으로 옮기는 역할을 가장 많이 했다.

「저어, 형님.」

“응, 왜?”

「그간 부끄러워서 말씀드리지 못했었는데…… 현재 몇몇 고위 장교들 사이에서 이런저런 말이 나오고 있는 것 같습니다.」

“말? 무슨 말?”

샤오 쉔이 내 눈치를 살피며 조심스럽게 속삭였다.

「그, 본인들이 맡은 역할에 불만이 조금…….」

“……?”

저게 도대체 무슨 소리지.

샤오 쉔의 말을 이해하기까지는 제법 긴 시간이 필요했다. 무거운 침묵이 흐른 뒤, 나는 설마 하는 마음으로 입술을 뗐다.

“혹시 자기들도 몬스터 사체 그만 치우고 공을 세우고 싶다. 뭐 그런 거야?”

「……예.」

“아니, 이런 미친 새끼들을 봤나.”

쌍욕이 절로 튀어나오는 상황이다. 다른 전선에서는 군인들이 하루가 멀다고 죽어 나가는데, 몬스터 사체 치우기가 지겹다니.

가만히 듣고 있던 최 팀장이 침착하게 입을 열었다.

“당황하지 마십시오. 짱깨가 짱깨 했을 뿐입니다.”

저게 천 명에 가까운 중국인들 앞에서 할 소린가 싶지만, 중국인과 짱깨는 엄연히 다른 인종이다.

착한 중국인의 대표인 샤오 쉔의 얼굴은 어느새 부끄러움으로 붉어져 있었다.

「죄, 죄송합니다. 다만 장교들 전부는 아니고, 일부 인원들이 그런 불만을 품은 것으로 알고 있습니다.」

“일부 인원들이라. 그렇겠지. 그런데 한 가지 궁금한 게 있는데…….”

나는 눈살을 찌푸리며 샤오 쉔의 어깨너머를 가리켰다.

“그 일부 인원에, 저기 오는 저 인간도 포함되어 있냐?”

저 멀리, 백여 대의 장갑차와 전차가 먼지구름을 일으키며 이곳을 향해 다가오고 있었다.



* * *



드르륵, 덜컹!

황폐해진 도로를 달리는 차량이 위아래로 들썩인다. 앉아 있는 군용 차량의 창밖으로 엉망이 된 논과 밭, 무너진 민가가 드문드문 보이기 시작했다.

뒷정리가 끝난 후 나는, 아니 ‘우리’는 인근 소도시로 향하는 중이었다.

「하하, 정말 고생 많았소이다. 진 선생!」

꽉 조인 벨트로도 감출 수 없는 뱃살. 태양 아래 번쩍이는 정수리.

입고 있는 군복과 견장에 박힌 별 세 개가 아니었다면, 내가 눈앞의 장년인과 만날 일은 없었을 것이다.

「안 그래도 오늘 아침 상부에 연락이 닿았소. 진 선생의 승전보에 유엔 안보리는 물론이고 전 세계가 난리가 났어요! 내 무슨 소리인지는 모르겠지만, 한국에서는 오늘을 주모 기일이라 부른다던데…….」

시종일관 떠들어 대는 헛소리를 듣는 건 여기까지다. 나는 참지 못하고 불쑥 입을 열었다.

“주모가 뒤졌는지 살았는지, 그런 건 관심 없고요. 하나만 물어봐도 됩니까?”

「지, 진 선생?」

중국 정식 편제로는 청두군구(成都軍球). 그중에서도 일곱 개의 사단, 여단이 속한 제 13집단군 총사령관인 랴오 상장은 불안한 눈빛으로 날 바라봤다.

「왜, 왜 이러시오? 무슨 일이라도 있었소?」

“오늘 제가 이상한 이야기를 들어서요. 지금 좀 예민해졌네요.”

「누가 감히 진 선생의 심기를! 뭐든 물어보시오.」

“아, 예. 제가 여쭤볼 건 다름이 아니고…….”

나는 기름기로 번들거리는 랴오 상장의 얼굴을 빤히 바라보며 말을 이었다.

“공을 세우고 싶은 몇몇 장교들의 불만이 상당하다던데…… 혹시 알고 계셨나 해서요.”

「크흠.」

알고 있었군. 그걸 알면서도 가만히 놔뒀다니. 하도 어이가 없으려니 이제는 오히려 덤덤해진다.

그래도 명색이 아군이자 타국의 쓰리스타. 나는 최대한 침착하고 공손한 어조로 물었다.

“그 씨팔 새끼들 면상 좀 볼 수 있습니까?”

「크흐흠!」

“아니 시부럴 거, 어떤 정신 나간 놈들이 이 시국에 공을 세우고 싶다고 지랄을 해요. 막말로 지들이 나가서 싸울 것도 아니고, 일반 병사들 앞에 세우고 뒤에서 지휘봉이나 휘두를 거 아닙니까.”

「크흐흐흠!」

“몬스터 사체 치우기 귀찮다는 게 무슨 개소립니까. 왜요, 하도 보니까 정겹고 친근해져서 본인들도 사체가 되고 싶대요? 진짜 뒈져 봐야 정신을 차리지. 개 같은 거.”

「크흐흐흐흠!」

“그런 새끼들 있으면 그냥 와서 말하라고 해요. 장비 입혀서 선봉에 세워 줄 테니까. 고기 방패로 쓰면 딱이겠…….”

열변을 토하던 나는 문득 입을 닫았다. 랴오 상장의 이마에서 식은땀이 스프링클러처럼 쏟아지는 중이었다.

「…….」

“…….”

이 인간도 그 정신 나간 놈 중에 하나구만.

지하 벙커에서 핵을 쏘니 마니, 염병을 할 때부터 보통 미친놈은 아니구나 싶었는데. 정말 상당한 수준으로 미쳐 있는 게 분명하다.

“……장군님. 제정신입니까?”

「그, 그러니까 이게. 우리도 뭔가를 보여 줘야 한다. 뭐 그런 게 조금은…….」

“아니, 피해 없이 쭉쭉 잘 가고 있는데 여기서 뭘 더 보여 줘요. 헌터들이 앞에서 길 뚫고, 군대는 뒤에서 뒷수습하면서 민간인들 구하고. 잘하고 있는데 뭘 더 보여 주냐고.”

우두둑.

손가락 관절을 꺾는 내 모습에 랴오 상장이 황급히 손을 내저었다.

「어, 어허! 우리 서로 간에 반말은 하지 맙시다. 내 연배로 보나 계급으로 보나, 진 선생에게 이런 대접을 받을 사람이 아니오.」

“아주 그냥, 대접으로 대가리를 깨 버릴까.”

「뭐, 뭣이?」

“아닙니다. 잘못 들으신 거예요. 어쨌든 알겠고, 허튼 생각하지 마십시오. 지금부터는 사상자는 최소로, 민간인들 구출하면서 천천히 진격하자고요. 아시겠습니까?”

「…….」

이 인간 반응이 왜 이래?

대답 대신 눈깔을 뒤룩뒤룩 굴리는 랴오 상장을 보는 순간, 등골이 서늘해졌다.

설마…….

“이미 명령을 내린 겁니까?”

「그, 그게. 내가 지금 군납 비리 건에 연루되어 있기도 하고. 독자적으로 뭔가를 해내야 하는 시점이라…….」

“야 이 개새끼야!”

쾅!

내 발길질에 방탄 처리 되어 있는 문짝이 뜯겨 나갔다. 앞 좌석에 앉아 있던 운전병이 황급히 브레이크를 밟았다.

끼이이익!

“히익!”

잔뜩 몸을 웅크린 채 벌벌 떨던 랴오 상장이 더듬거리는 목소리로 대답했다.

「우, 우리가 지금 가고 있는 소도시에 몬스터가 있을 것 같아서 예비대로 운용 중이던 공안 무력부 헌터들을 조금 투입시켰…….」

더 들을 필요도 없었다. 내가 뭐라 다그치기도 전에, 어느새 가까워진 도시로부터 굉음이 울려 퍼졌으니까.

콰아아앙!

거대한 폭발. 솟구치는 불꽃과 연기.

그리고…….

띠링.

돌발 퀘스트를 알리는 시스템 알림이 있었다.
```

## Final English reading copy

```markdown
# Chapter 390

Whoosh!

Where the blade force swept past, hot blood spurted as heads sprang into the air.

I stepped on the ogre’s body as it collapsed like a bundle of straw and sprang high into the air. The sunlight touching the back of my neck was warm.

*Perfect weather for a fight.*

It was noon. The location was a wasteland without a single tree.

With the sun at my back, my shadow fell across the midst of the thousand or so monsters gathered below—even the spearhead in it slashing downward as I dove.

*Heavenly Strike.*

Boom!

The Flame Dragon’s Claw raked across the earth.

The roar sounded as if the sky itself had split apart. The ground sank several meters, sending dirt and fragments of stone flying in every direction.

A vortex of hot air that erupted at the center of the battlefield became a blade and swept through the monsters.

Boom!

Ding. Ding. Ding…

Through my dust-clouded vision, green blood poured down in rapid splatters as System notifications announced the monsters’ deaths.

I waved my hand lightly, scattering the dust cloud. The monsters staring at me with blank faces came into view.

“Chirrik?”

“Krrk?”

Their eyes seemed to ask what the hell had just happened. I drew in a deep breath, then shouted with my internal energy behind my voice.

“Wipe them out—!”

And then—

“Waaaaaaah!”

With an earsplitting roar, more than a thousand Hunters who had rushed in by then descended on the monster army like a wave.

Crack-crack-crack!

Wham!

Watching the monsters crumble helplessly, I became certain of one thing.

*We’ve won this battle.*

The farming was over. Now it was time to harvest.

I headed toward the Twin-Headed Ogre that looked like the boss monster.

For the sake of my precious EXP. No—for the sake of minimizing our casualties.

“That one’s the leader! Ranged units!”

“Hey, hey! Hands off! I’ll take care of it, so don’t touch a single hair on its head!”

I swear to heaven, I had not a shred of ulterior motive.

…

Well, after thinking about it, I didn’t need to swear.

“Insidious human. Your intention to claim the byproducts is painfully obvious. You didn’t conceal your greed even while slaughtering my legion!”

“Shut up and do your job. Hurry up and start making your kind kill each other as undead.”

“I was going to do that anyway. Grow, my sea of skeletons… Huh?”

“What’s wrong?”

“Why isn’t my power working? Is this perhaps a bug?”

“…”

“Where did you even pick up a word like that?”

The Skeleton Warlord, whose modernization was progressing by the day, spoke in a dejected voice.

“The farther inside I go, the stronger the Arch Lich’s control seems to become. Ah, a commander without a legion. Truly, I cannot contain my grief. At this rate, I might as well be dead!”

“…”

What the hell did this guy think he was?

I was tired of telling him that he was already dead. Sighing inwardly, I charged at the leader.

* * *

“It’s a crushing victory! Another crushing victory!”

Shao Shen shouted with a flushed face. We had seen this scene more than ten times by now, so Team Leader Choi and I had reached the point where we simply took it in stride.

*Well, I can understand why he’s excited.*

It had taken barely two hours to annihilate an army of more than a thousand monsters.

And we had finished without a single death. It really was a victory worth commemorating. In a situation like this, acting calm would be stranger.

“Our casualties are only twenty-three seriously wounded and thirty lightly wounded. Ah, this is really…!”

Shao Shen trembled like a dog desperate to pee and stared at me with shining eyes.

“How can this happen every time?”

“Hmm. Maybe it’s because I’m strong.”

Team Leader Choi gave me a slightly incredulous look.

“Why?”

“Usually, this is when people say something modest, like that they were lucky.”

“Usually, yes. But it’s not that I’m lucky. I’m genuinely strong. What else can I do? Isn’t that right, Shen?”

Shao Shen nodded at tremendous speed.

“That’s right! Hyung-nim is the best!”

“Good lad. You’re a fine specimen of flattery.”

“…”

Team Leader Choi shook his head as he watched us trade lines back and forth.

“What?”

“Nothing. Though I suppose this is very much like you, Mr. Jin Taekyung.”

Somehow, that sounded vaguely insulting.

I shrugged and turned to Shao Shen.

“More importantly, what about headquarters?”

“Ah, yes. I contacted them before the battle began.”

Contacting them meant that he had sent several Hunters under his command ahead of us.

In this day and age, sending messengers seemed ridiculous, but there was no choice. Magic had made communication and satellite surveillance impossible, so we either had to run ourselves or use vehicles.

At least we still had things like signal flares.

“It’ll take a while.”

“They were already following us, so it shouldn’t take too long.”

“You’re tired, but put up some tents and let the men rest. The battle ended quickly, but fighting drains you completely.”

“Shouldn’t we take care of the large monsters ourselves? It might be difficult for headquarters to move otherwise…”

“That’s a fair point.”

Headquarters referred to the military forces moving with us.

When Hunters from the Public Security Armed Forces, myself included, defeated the monsters at the front, the military forces following behind would “clean up” the area and the monster corpses.

The reason I called it cleaning was that the purpose wasn’t to collect the byproducts.

It was literally cleanup. The army assigned to my western front spent most of its time chopping up the dead monsters so they couldn’t be resurrected as undead, then transporting the remains to the rear.

“Hyung-nim.”

“Yeah? What is it?”

“I was too embarrassed to mention this before, but… it seems that some of the senior officers have been making various complaints.”

“Complaints? What kind?”

Shao Shen glanced at me and lowered his voice cautiously.

“They’re… somewhat dissatisfied with the roles they’ve been assigned.”

“…”

What the hell was he talking about?

It took me a while to understand Shao Shen’s words. After a heavy silence passed, I finally parted my lips, half expecting the worst.

“Do they want to stop cleaning up monster corpses and earn some merit themselves?”

“…Yes.”

“Are you fucking kidding me?”

The profanity came out on its own. Soldiers were dying every day on the other fronts, and these people were complaining that cleaning up monster corpses was boring.

Team Leader Choi, who had been listening quietly, spoke in a calm voice.

“Don’t be alarmed. The chinks are just being chinks.”

I wondered if that was really something he should say in front of nearly a thousand Chinese people. But Chinese and chinks were, strictly speaking, two entirely different races.

Shao Shen, the model Chinese man, had gone red with embarrassment.

“I-I’m sorry. But I understand that not all the officers are like that. Only some of them have those complaints.”

“Some of them, huh. I’m sure that’s the case. But there’s something I’m curious about…”

I frowned and pointed over Shao Shen’s shoulder.

“Does that include the guy coming over there?”

In the distance, more than a hundred armored vehicles and tanks approached us, raising a cloud of dust.

* * *

Rattle, clunk!

The vehicle bounced up and down as it raced along the ruined road. Through the window of the military vehicle I was sitting in, I began to see ruined rice paddies and fields, along with collapsed houses scattered here and there.

After the cleanup was finished, I—or rather, *we*—were heading toward a nearby small city.

“Ha-ha! You’ve really worked hard, Teacher Jin!”

A belly that even a tightly fastened belt couldn’t conceal. A bald crown gleaming beneath the sun.

If not for the military uniform he wore and the three stars on his shoulder strap, I would never have had any reason to meet the middle-aged man in front of me.

“I contacted the higher-ups this morning, as it happens. The entire world, not to mention the United Nations Security Council, is in an uproar over Teacher Jin’s victory report! I don’t know what they mean, but apparently people in Korea are calling today Jumo’s death anniversary…[^1]

[^1]: *Jumo* is a traditional tavern keeper. Koreans jokingly call for her to serve drinks online when celebrating a national triumph.”

I had reached my limit for listening to his nonstop stream of nonsense. Unable to hold back any longer, I cut in.

“I don’t care whether the tavern lady is dead or alive. Can I ask you one thing?”

“Te-Teacher Jin?”

Under China’s official military structure, this was the Chengdu Military Region. More specifically, the man before me was Senior General Liao, commander-in-chief of the Thirteenth Group Army, which included seven divisions and brigades.

He looked at me anxiously.

“Why, why are you acting like this? Did something happen?”

“I heard something strange today, so I’m a little sensitive right now.”

“Who dared upset Teacher Jin? Ask me anything.”

“Yes. What I wanted to ask is…”

I stared at Senior General Liao’s greasy, glistening face and continued.

“I heard that some officers are extremely dissatisfied because they want to earn merit. Did you know about that?”

“Ahem.”

So he knew.

He had known about it and still done nothing. It was so absurd that I had passed beyond anger and reached a state of numbness.

Still, he was technically an ally and a three-star general from another country, so I asked as calmly and politely as I could.

“Could I see the faces of those fucking bastards?”

“Ahem!”

“What kind of lunatics are throwing a fit about wanting to earn merit at a time like this? To put it bluntly, they aren’t going to fight themselves. They’ll just put ordinary soldiers in front and wave their command batons from behind, won’t they?”

“Ahem! Ahem!”

“What the fuck does it mean that they’re tired of cleaning up monster corpses? What, have they seen so many of them that they’ve grown fond of them and want to become corpses themselves? They’ll have to actually die before they come to their senses. Goddamn it.”

“Ahem! Ahem! Ahem!”

“If there are any of those bastards, tell them to come see me. I’ll equip them and put them in the vanguard. They’d make perfect meat shields—”

I suddenly shut my mouth.

Cold sweat was pouring from Senior General Liao’s forehead like water from a sprinkler.

…

“…”

This man was one of those lunatics too.

I’d suspected he was no ordinary madman ever since he’d kicked up that whole goddamn fuss in an underground bunker over whether or not to launch a nuke. But he was clearly insane on an entirely different level.

“General, are you in your right mind?”

“Well, that is… We also have to show them something. We have to prove that we can do something too…”

“No casualties, everything moving forward smoothly—what more do you want to show them? The Hunters are breaking through the path ahead, while the army is cleaning up behind them and rescuing civilians. We’re doing a good job. What else do you want to show?”

Crack.

I cracked my knuckles. Senior General Liao hurriedly waved his hands.

“Now, now! Let’s not speak informally to each other. Whether you consider my age or my rank, I’m not someone who should be treated this way by Teacher Jin.”

“How about I crack your skull open with a serving bowl?”

“Wh-What?”

“Nothing. You heard me wrong. Anyway, I understand. Don’t entertain any foolish ideas. From now on, let’s advance slowly, minimize casualties, and rescue civilians. Understood?”

“…”

What was wrong with this man’s reaction?

The moment I saw Senior General Liao’s eyes rolling around instead of answering, a chill ran down my spine.

*No way…*

“Have you already issued an order?”

“Well, I’m currently involved in the military procurement corruption scandal too. It’s time for me to accomplish something independently…”

“You fucking bastard!”

Bang!

My kick tore the armored door off its hinges. The driver sitting in the front seat hurriedly slammed on the brakes.

Screech!

“Eek!”

Senior General Liao huddled up and trembled as he answered in a stammering voice.

“I-I thought there might be monsters in the small city we’re heading toward, so I deployed some of the Public Security Armed Forces Hunters who had been held in reserve…”

I didn’t need to hear any more. Before I could press him further, a roar rang out from the city that had suddenly drawn close.

Boom!

A massive explosion. Flames and smoke surged into the sky.

And then—

Ding.

A System notification announced an Unexpected Quest.
```
