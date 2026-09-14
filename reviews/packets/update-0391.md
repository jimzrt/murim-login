<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0391.txt",
      "sha256": "d9215c15667272c87d83f4f48f8e8481e65698634dac0073a4d39c57aa28c9ce",
      "bytes": 14274
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "af676eb305c71bccd46084be00a67c1bff007872d9ac1fd701ee0ff36b2fa4f7",
      "bytes": 5694
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "73a42ae057c92dc278779dbb3bd4b85b2385b71d0806b953271b74c7ef2a8001",
      "bytes": 13970
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3f87b9f50d6a7180155c5701d3880c89270729ef4a4f7f806517da7bf2f6ed28",
      "bytes": 10637
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 16001
}
-->

# Durable State Update — Chapter 391

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 391. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 391. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 391,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 391,
    "continuity_sources": [391],
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
    "Sichuan Province remains in a wartime state after the monster wave began in Gaoping District, Nanchong City; China has declared martial law and United Nations peacekeeping forces have joined the front.",
    "Wei Penghu is a Senior General and Minister of Defense at the Central Military Commission; Xiao Yang is Chairman of the Central Military Commission, General Secretary, and state chairman of China.",
    "Team Leader Choi trusts Taekyung, was rescued by him from a drinking-game predicament, and agreed to adjust Taekyung's settlement share to nine-to-one.",
    "The six S-rank Hunters were assigned to six fronts; Prince Felix left before dawn after receiving a battle signal.",
    "Magic Johnson is an S-rank Hunter, one of three Archmages worldwide, and a combat-specialized War Mage; Pai Chen is an S-rank Hunter and Great Cataclysm hero; Wu Heixing is an arrogant S-rank Hunter from a powerful Chinese Communist Party family.",
    "Prince Felix Alexander Louis is a British prince, third in line to the throne, and holds multiple senior British titles; William serves as his formal attendant.",
    "The Sichuan Tang Clan was devastated by Dark Heaven, owes Taekyung's group a debt, and is considering relocation.",
    "The Chengdu International Airport attack involved an undead army controlled by three incomplete Arch Liches, all of whom Taekyung destroyed.",
    "The Skeleton Warlord absorbed the death energy of the remaining two Arch Liches and became much stronger, but the Arch Lich's control now prevents him from raising undead deeper inside the army.",
    "Dark Heaven's agents, purpose, and connection to the hidden transport formation remain unresolved.",
    "Lee Jungryong is the practical leader of Ares Guild and one of the world's top three S-rank Hunters; he recognizes Choi Minwoo's growth and that Jin Taekyung has crossed the wall.",
    "Wu Heixing used Sound Transmission and martial-arts knowledge, attacked Taekyung, and was defeated after Taekyung took his Supreme Potion and left him with an Advanced Potion.",
    "An unrefusable Unexpected Quest, The Battle Situation Has Become Critical, previously ordered Taekyung to reach the battlefield quickly and defeat the enemies.",
    "Taekyung's western-front force annihilated more than a thousand monsters in roughly two hours without fatalities; twenty-three Hunters were seriously wounded and thirty lightly wounded, while the following army handled corpse cleanup.",
    "Senior General Liao commands the Chengdu Military Region's Thirteenth Group Army, knew some senior officers wanted combat merit, and secretly deployed reserve Hunters toward a nearby city while implicated in a military procurement corruption scandal.",
    "A massive explosion in the nearby city triggered a new Unexpected Quest; its objective, the reserve Hunters' fate, and its consequences remain unresolved."
  ],
  "continuity_sources": [
    390
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved.",
    "Dark Heaven's larger purpose, its reason for sparing Taekyung, and the origin and function of the hidden transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination, along with the timing and outcome of the Samgoe escort to Henan, remain unresolved.",
    "The request Dongbong wants to make of Taekyung, Mungyeong's eventual response to the coming war, and the identity and fate of the boy from the Chengdu port remain unresolved.",
    "Ae-hyang's superior and the consequences of the Sichuan Governor's false memorial remain unresolved.",
    "The relationship between the Lich and the Arch Lich, the full extent of the Skeleton Warlord's increased power, and the monster wave's larger plan remain unresolved.",
    "Lei Fei's fate and the fate of the missing Sichuan Hunters remain unresolved.",
    "The subject and consequences of Lee Jungryong's discussion with Wu Heixing, Wu Heixing's reason for sending the Sound Transmission, and the objective and consequences of the new Unexpected Quest remain unresolved."
  ],
  "safe_through": 390,
  "temporary_decisions": [
    "Render Zhonghua as Zhonghua and preserve the Jongseok mishearing joke for 총서기.",
    "Render Xiao Yang's offices as Chairman of the Central Military Commission, General Secretary, and state chairman.",
    "Render 대마법사 as Archmage and 워 메이지 as War Mage.",
    "Retain Teacher Jin for 진 선생, Comrade Chairman for 주석 동지, hyung-nim for 형님, and Jung Dragon for 정 드래곤.",
    "Render 반도의 빵즈 as peninsula bangzi and 짱깨 as chink or chinks, preserving the derogatory register.",
    "Preserve Taekyung's conversational, self-mocking first-person voice and the source's jokes, including the forum's exaggerated online register.",
    "Render established names and titles consistently, including Pai Chen, Wu Heixing, Prince Felix Alexander Louis, William, Senior General Liao, the Princelings, the Shanghai clique, Sound Transmission, Sword Force, Advanced Potion, Supreme Potion, and The Battle Situation Has Become Critical.",
    "Render 천격 as Heavenly Strike, 화룡의 발톱 as Flame Dragon's Claw, and 주모 as Jumo with the established explanatory footnote."
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
| 천격 | **Heavenly Strike** | Named spear technique used by Taekyung. |
| 화룡의 발톱 | **Flame Dragon's Claw** | Named technique invoked through Taekyung's spear attack. |
| 주모 | **Jumo** | Traditional tavern keeper in the Korean victory-day joke. |
| 청두군구 | **Chengdu Military Region** | Chinese military region commanded by Senior General Liao. |
| 제 13집단군 | **Thirteenth Group Army** | Army commanded by Senior General Liao. |

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
| 진태경 | 랴오 상장 | foreign_hero_to_allied_senior_general | General | hostile-but-formal | Taekyung uses 장군님 while confronting Liao over the reckless deployment. |

## Exact glossary matches

| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 탱커      | **tank**              |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 데스나이트 | **Death Knight** | Powerful undead being the three beings plan but fail to create. |
| 상장 | **Senior General** | Wei Penghu's military rank, explained as four-star. |
| 태자당 | **Princelings** | The Communist Party's largest faction; Liao belongs to it. |

## Listed compact profiles

(No chapter-safe profiles matched.)

## Korean source

```text
＃391화



후위에 남아 있던 쓰촨성 공안 무력부 2중대장, 장 웨이는 처음부터 이 작전이 꺼림칙했다.

‘군대와 함께 먼저 가서 도시를 점령하라니? 샤오 연대장이 내린 명령과는 다른데.’

장 웨이가 품고 있던 한 줄기 의문이 더욱 커진 것은, 굳이 앞에서 교전 중인 아군을 우회하여 진격했을 때부터였다.

「왕 상교(上校)님. 이 작전, 저희 연대장님께서 동의하신 게 확실합니까?」

장 웨이의 물음에 중년의 고위 장교가 눈살을 찌푸리며 대답했다.

「왜 그런 게 궁금하지?」

「아무리 생각해도 이상해서 말입니다. 분명히 저희 연대장님께서는 후위에서 체력을 비축하며 본부를 호위하라고 하셨는데…….」

「아, 그 꼬마 연대장 말이지.」

샤오 쉔을 향한 고위 장교의 비웃음에 장 웨이가 얼굴을 굳혔다.

「샤오 쉔 연대장은 왕 상교님과 같은 계급입니다. 그것도 곧 소장 진급을 앞두고 계신.」

「세상 물정 모르는 어린 애가 운이 좋았던 게지. A급 헌터로 각성한 것으로도 모자라, 한국 놈이 활약해 준 덕분에 덩달아 이번 진급 명단에도 올랐으니. 이렇게 초고속 승진을 하는 걸 보니까 정계에 괜찮은 꽌시(关系)라도 있는 건가?」

「……나이는 어리지만 그만큼 뛰어난 분입니다. 저희와도 형제처럼 지내실 만큼 신망도 두텁고요.」

고위 장교가 손에 든 지휘봉을 쓸어내렸다.

「헌터들 위아래 없는 거야 본관도 잘 알고 있네. 하지만 지금은 전시 상황이야. 이 명령은 사령관이신 랴오 상장께서 내리신 거고.」

「사령관님께서 직접…… 말씀이십니까?」

「그래. 그러니 명령에 따르기 싫다면 지금이라도 돌아가게. 단, 지금 자네의 행동이 명령 불복종이라는 사실을 알고 있기를 바라지.」

「……!」

「진격 속도를 좀 더 단축하고자 할 뿐이야. 정황상 그럴 리는 없겠지만 몬스터 잔당이 남아 있다면 쓸어 버리고, 위험에 빠진 민간인들을 구출하는 게 전부라고. 알아들었나?」

한참이나 말이 없던 장 웨이는 고개를 끄덕이고 물러났다.

일반적으로 공안 무력부는 군부에 속하지 않은 별개의 단체로 취급받지만, 현재는 전시 상황이었다. 서부 전선 사령관인 랴오 상장의 명령을 거스르는 건 결코 좋은 선택이 아니었다.

「뭐랍니까?」

한껏 목소리를 낮춘 부하의 물음에 장 웨이가 대답했다.

「쉬운 작전이니 닥치고 따라오라는군. 거절하면 명령 불복종이고.」

「그 말을 믿으십니까?」

「전자를 묻는 거라면 당연히 아니지. 하지만 후자는 사실일 거야. 자네는 어떻게 생각하나?」

「당연히 못 믿죠. 왕 상교 저놈, 능력도 없는 주제에 태자당 쪽 꽌시 하나로 여기까지 올라온 놈입니다. 랴오 상장이 기르는 충견이라고 소문이 자자해요.」

「바로 그 랴오 상장의 명령이야. 당장은 구린내가 나더라도 참을 수밖에.」

「……빌어먹을.」

「하지만 왕 상교의 말이 사실일지도 몰라. 인근에 존재하는 대부분의 몬스터는 전부 아군과 교전 중일 테니까. 현재 우리 전력이라면 몬스터 잔당 정도는 충분해.」

장 웨이는 주위를 둘러보았다. 그를 포함한 백 명의 헌터 외에도 이십여 대의 전차와 오백의 보병. 상공에는 전투 헬기 세 대가 시야를 확보하며 나아가는 중이었다.

‘부디 별다른 피해가 없기를.’

장 웨이의 바램이 하늘에 닿았는지, 그가 우려하던 일은 발생하지 않았다.

촉각을 곤두세우며 진입한 쑤이닝시 인근의 작은 소도시는 몬스터에 의해 초토화된 상태였을 뿐, 폐허가 된 도심은 적막하기 그지없었다.

고블린, 오크 따위의 몬스터가 간간이 튀어 나왔지만, 그들에게는 아무런 위협도 되지 못했다.

- 키이이익!

서걱!

가장 선두에서 십여 마리의 몬스터들을 처치한 장 웨이는 약간 이나마 마음이 풀어졌다.

「종도 다른 몬스터가 따로따로 나타나는 걸 보니 무리에서 이탈한 놈들 같군요.」

「예상대로군. 그러게 내가 뭐라고 했나?」

거만하게 대답하는 꼴이 썩 마음에 들지 않았지만, 차라리 이게 낫다.

그렇게 생각하고 잠자코 고개를 끄덕이던 장 웨이는 이어지는 고위 장교의 말에 멈칫하고 말았다.

「병력을 나누라고 하셨습니까?」

「그래. 이런 상황이라면 최대한 빨리 생존자부터 찾아야지.」

「하지만 왕 상교님. 진입한 지 아직 한 시간도 채 되지 않았습니다. 조금 더 중심부로 나아간 후에…….」

「건방진 소리.」

「예?」

「전투 실력은 헌터인 자네들이 나을지 몰라도, 전술은 내가 몇 수 위야. 현재 지휘권은 내게 있으니 그만 입 다물고 명령을 따르라고.」

「……!」

「못 들었나? 그럼 본관이 직접 자네 수하들에게 명령을 내릴까?」

「……제가 하지요.」

「세부 지도는 갖고 있겠지. 그럼 두 시간 후에 중앙 광장에서 보도록 하지.」

장 웨이를 향해 밉살맞게 웃어 보인 장교가 장갑차에 몸을 실으려던 그 순간이었다.

쐐애애액, 펑!

장 웨이는 멍하니 눈을 깜빡였다. 손바닥으로 얼굴을 쓸어내리자 끈적한 핏물이 한가득 묻어 나왔다.

한없이 붉은색을 띤 그것은 분명 인간의 것이었고, 이미 상반신이 흔적도 없이 사라진 장교의 몸뚱어리는 장갑차에서 굴러떨어지고 있었다.

쿵.

숨 막히는 정적. 가장 먼저 정신을 차린 장 웨이가 외쳤다.

「전원 전투 준비-!」

「몬스터! 몬스터가 나타났다!」

「탱커!」

「여, 연대장님께서 전사하셨다!」

그 외침에 가장 먼저 반응한 것은 공안 무력부의 헌터들이었고, 군인들은 한차례 늦게 상황을 파악했다.

그리고 갑작스러운 지휘관의 사망으로 극심에 혼란에 빠진 그들을 기다리고 있던 것은 더욱 처절한 죽음이었다.

쐐애애액!

단 한 번의 파공성.

보이지도 않는 속도로 쏘아진 빛줄기가 오와 열을 맞춘 채 진군 중이던 군인들을 휩쓸었다.

퍼버버벙!

수십의 사람들을 풍선처럼 터트리며 나아간 빛줄기가 마지막으로 꿰뚫은 것은 보병들의 호위를 받으며 이동하던 장갑차였다.

단단한 외피를 뚫고 내부 깊숙이 파고든 빛줄기. 그 광경을 목격한 장 웨이가 벼락처럼 외쳤다.

「모두 피해!」

그러나 그의 외침이 닿기도 전에, 다음 순간 터져 나온 굉음이 모든 것을 집어삼켰다.

꽈아앙!

붉은 섬광, 검은 연기와 함께 터져 나간 장갑차의 파편이 수백, 수천 개의 칼날이 되어 사방을 난자한다.

군인은 물론이고 미처 반응하지 못한 하급 헌터까지. 셀 수도 없는 이들이 짚단처럼 쓰러졌다.

이미 숨이 끊긴 그들의 몸뚱어리는 미동조차 하지 않았다.

「……!」

「이, 이게 도대체…….」

석상처럼 굳어 버린 사람들을 향해 장 웨이가 고함을 내질렀다.

「산개! 모두 산개해라! 전차와 장갑차에서 최대한 멀리 떨어져!」

하지만 난생처음으로 실전을 겪는 병사들의 몸은 굳어 있었고, 아직 모습을 드러내지 않은 상대는 적들의 혼란을 결코 놓치는 법이 없었다.

쐐애애애액!

다시 한번 들려오는 죽음의 소리. 그러나 지금까지와는 달리 쏘아진 빛줄기는 하나가 아니었다.

콰앙! 퍼버버벙!

「크아아아악!」

불꽃이 솟구치고 비명이 넘쳐흐른다.

이십여 대의 장갑차와 전차가 무력화되기까지 걸린 시간은 그야말로 찰나.

상공을 배회하던 세 대의 전투 헬기 역시 수많은 파편으로 화해 지상으로 추락했다.

콰앙! 투두두둑.

시산혈해라고 부를 만한 참혹한 현장에, 장 웨이는 등골을 타고 흐르는 오싹한 기운을 느꼈다.

‘최소 A급 몬스터. 그것도 한둘이 아니다.’

아이러니하게도, 그것이 오늘 장 웨이가 내린 판단 중 가장 정확한 것이었다.

스아아아아.

어두컴컴한 골목과 무너진 건물 사이. 아직도 타오르는 빌딩의 옥상.

검은 안개처럼 나타난 열 개의 형체들은 타오르는 보랏빛 안광으로 살아남은 수백의 인간들을 응시했다.

뼈밖에 남지 않은 전마(戰馬)에 올라탄 형체들을 발견한 장 웨이의 입술 사이로 신음 같은 한 마디가 새어 나왔다.

「……데스나이트(Death Knight).」

한때는 고결했으나 흑마법에 의해 타락한 죽음의 기사들.

리치와 함께 대격변 이후 모습을 감춘 바로 그 데스나이트가 나타났다. 그것도 자그마치 열 기나 되는 숫자.

순간 장 웨이의 머릿속에 가장 먼저 떠오른 단어는 죽음이었다.

‘여기까지인가.’

데스나이트는 A급 몬스터를 벗어난 존재들이다.

아직 백 명의 헌터와 군병력이 남았지만, 장 웨이는 이미 알고 있었다.

놈들이 펼쳐 놓은 그물을 피할 수 없다는 사실을.

하지만…….

「곱게 죽어 줄 생각 따위는 없다.」

그것은 비단 장 웨이만의 생각이 아니었다.

두려움으로 총기조차 제대로 잡지 못하는 군인들과 달리, 공안 무력부의 헌터들은 결의에 찬 눈빛으로 각자의 병장기를 치켜세웠다.

「너희까지 이럴 필요는 없어.」

장 웨이의 나지막한 한마디에, 소대장 중 하나가 퉁명스럽게 대답했다.

「중대장님은 이래도 되고요?」

「미안하다. 너희를 데려오는 게 아니었는데.」

「누가 데려온 게 아니라, 저희가 따라온 겁니다. 중대장님 덕분에 열 번도 넘게 살아남았으니 한 번쯤 이럴 때도 됐죠.」

아무렇지 않게 말하지만, 목소리에 묻어 나오는 떨림마저 감출 수는 없었다.

미동도 하지 않는 열 기의 데스나이트를 바라보며, 장 웨이는 바짝 마른 입술을 핥았다.

「최선을 다해 싸우고, 한 사람이라도 살아남아라. 너희에게 해 줄 말은 그게 전부다.」

대답 대신 우렁찬 함성이 터져 나왔다. 두려움을 몰아낸 헌터들의 눈동자가 샛별처럼 빛났다.

안전하고 풍요로운 삶을 원했다면 다른 길도 있었다.

그러나 그들이 부유한 기업가의 경호원이나, 용병 대신 공안 무력부를 택한 것은 헌터로서의 명예와 책임감 때문이었다.

이건 결코 물러설 수 없는 싸움이다.

「가자! 인민의 아들딸, 중화의 후예들이여!」

온 힘을 다해 부르짖은 장 웨이가 가장 가까운 데스나이트를 향해 쇄도하려던 바로 그 순간.

구구구구궁!

그건 본능에 가까웠다.

거센 진동과 함께 느껴지는 거대한 기운. 살아남은 인간들은 전신의 털이 쭈뼛 곤두서는 공포와 함께 고개를 돌렸다.

여러 눈동자가 향하는 곳에, 폐허가 된 도심지를 천천히 가로지르는 검은 기사가 있었다.

깊게 눌러쓴 투구 아래, 붉은 안광이 번쩍인다. 핏기없는 입술 사이로 죽음의 숨결이 뿜어져 나왔다.

- 사르, 가로쉬.

누구도 알아들을 수 없는 마계의 언어.

그러나 다음 순간, 장 웨이는 곧 그 말이 무엇을 뜻하는지 깨달을 수 있었다.

‘모두 죽여라.’

부릅떠진 장 웨이의 눈동자에, 사방에서 쇄도해 오는 열 기의 데스나이트가 비쳤다.

서걱!

도륙의 시작이었다.



* * *



철벅.

뼈밖에 남지 않은 말발굽이 피 웅덩이를 밟았다.

마지막까지 저항하던 중년의 헌터, 장 웨이의 시신을 물끄러미 내려다보는 검은 기사를 향해 다가온 데스나이트들이 한쪽 무릎을 꿇었다.

- 로드. 다음 명령을.

다음 명령이라.

잠시 말이 없던 검은 기사가 문득 손을 뻗었다.

쉬익, 서걱!

채찍처럼 휘둘러진 흑색 빛줄기가 콘크리트와 철근을 갈랐다.

비스듬히 허물어지는 건물. 드러난 내부 공간에는 한껏 입을 막은 채 웅크려 있는 인간들이 있었다.

「진진. 여보. 괜찮아, 괜찮아…….」

「흑, 흐흐흑!」

「압빠빠?」

인간 수컷과 암컷. 그리고…… 아직 암수 구분이 되지 않을 만큼 한없이 작고 가벼워 보이는 존재.

아마 저걸 아이라고 하던가.

‘아이, 아이?’

이 단어를 어디서 들어 봤던가.

검은 기사는 문득 드는 의문을 뒤로하고 손을 뻗었다. 눈에 보이는 인간은 말살시켜야 한다. 그것이 그가 받은 명령이었다.

하지만.

- ……?

어째서인지 손이 나아가지 않았다.

손가락만 튕겨도 한 줌 핏물로 화해 사라질 나약한 존재들이 분명한데, 마치 보이지 않는 방어막이 인간들을 감싸고 있는 듯했다.

- 너희는. 뭐지?

검은 기사의 음산한 목소리에 부모의 품 안에서 꼬물거리던 아이가 으앙, 하고 소리 내어 울음을 터트린 그때였다.

- 이건.

문득 고개를 들어 저 너머를 바라보던 검은 기사가 말머리를 돌렸다.

갑작스러운 우두머리의 행동에 데스나이트들이 의문을 표했다.

- 로드?

- 돌아간다. 지금. 당장.

- 그럼 인간들은 저희가.

- 돌아간다. 지금. 당장.

그것이 전부였다. 무릎을 꿇어 예를 표한 열 기의 데스나이트는 우두머리의 뒤를 따라 말을 달렸다.

그들의 모습이 안개처럼 사라지기 직전, 검은 기사의 붉은 안광이 기적처럼 살아남은 세 인간에 닿았다가 떨어졌다.

휘이이이잉.

피비린내를 머금은 바람이 시체로 가득한 폐허를 휩쓸었다.
```

## Final English reading copy

```markdown
# Chapter 391

Zhang Wei, commander of the 2nd Company of the Sichuan Province Public Security Armed Forces, had felt uneasy about this operation from the very beginning.

*Advance ahead with the army and seize the city? That’s different from the order Regimental Commander Shao gave me.*

The doubt Zhang Wei had been harboring only grew when they deliberately bypassed the allied forces engaged in combat ahead of them and continued their advance.

“Senior Colonel Wang. Are you certain our regimental commander approved this operation?”

The middle-aged senior officer frowned at Zhang Wei’s question.

“Why are you curious about that?”

“No matter how I look at it, something seems wrong. Our regimental commander clearly told us to conserve our strength in the rear and guard headquarters…”

“Ah, you mean that little regimental commander.”

Zhang Wei’s expression hardened at the senior officer’s mocking tone toward Shao Shen.

“Regimental Commander Shao Shen holds the same rank as you, Senior Colonel Wang. And he’s about to be promoted to major general.”

“That ignorant child was simply lucky. Awakening as an A-rank Hunter wasn’t enough—thanks to that Korean bastard’s performance, he even ended up on this promotion list. Considering how quickly he’s risen through the ranks, I wonder if he has some decent guanxi in political circles.”[^1]

“He may be young, but he’s just as capable. He’s also well respected enough that he treats us like brothers.”

The senior officer stroked the baton in his hand.

“I know Hunters don’t recognize rank and seniority the way ordinary soldiers do. But this is wartime. This order came from Senior General Liao, the commander.”

“From the commander himself…?”

“That’s right. So if you don’t want to follow the order, turn back now. But I hope you understand that what you’re doing constitutes disobeying orders.”

“……!”

“I merely want to shorten our advance time. The circumstances make it unlikely, but if any monsters remain, we’ll wipe them out and rescue any civilians in danger. That’s all. Understood?”

Zhang Wei remained silent for a long while before nodding and stepping away.

The Public Security Armed Forces were generally treated as a separate organization outside the military, but this was wartime. Defying Senior General Liao, the commander of the western front, was by no means a wise choice.

“What did he say?”

A subordinate asked in a lowered voice. Zhang Wei answered.

“He says it’s an easy operation, so we should shut up and follow him. Refusing would constitute disobedience.”

“Do you believe him?”

“If you’re asking about the first part, of course not. But the second part is probably true. What do you think?”

“Of course I don’t believe him. That bastard Senior Colonel Wang has risen this far on a single connection to the Princelings despite having no ability. Everyone says he’s Senior General Liao’s lapdog.”

“And this is an order from that very Senior General Liao. We’ll have to endure it for now, even if it smells rotten.”

“Damn it.”

“But Senior Colonel Wang might be telling the truth. Most of the monsters in the area are probably engaged with our forces. With our current strength, we should be more than capable of handling a few stragglers.”

Zhang Wei looked around him. In addition to the hundred Hunters, including himself, there were around twenty tanks and five hundred infantrymen. Three combat helicopters were advancing overhead, securing their field of vision.

*Please, let there be no casualties.*

Perhaps Zhang Wei’s wish had reached the heavens. The thing he had feared did not happen.

The small town near Suining City, which they entered with every sense alert, had been utterly devastated by monsters. Apart from that, the ruined downtown area was deathly silent.

Monsters such as goblins and orcs occasionally sprang out, but they posed no threat whatsoever.

—Kieeeek!

Slice!

After killing a dozen or so monsters at the very front, Zhang Wei felt slightly more at ease.

“Seeing how monsters of different species are appearing separately, they must be stragglers that broke away from the main group.”

“Just as expected. What did I tell you?”

The officer’s arrogant manner was irritating, but this was still preferable.

Thinking so, Zhang Wei silently nodded. Then he froze at the senior officer’s next words.

“You want us to split up our forces?”

“That’s right. In a situation like this, we need to find survivors as quickly as possible.”

“But Senior Colonel Wang, we haven’t even been inside for an hour yet. We should advance a little farther toward the center first…”

“Impertinent.”

“Pardon?”

“You Hunters may be better at combat, but I’m several moves ahead of you when it comes to tactics. I hold command authority at present, so stop talking and follow my orders.”

“……!”

“Didn’t you hear me? Should I issue the order directly to your subordinates?”

“…I’ll do it.”

“You have a detailed map, I assume. Then we’ll meet at the central square in two hours.”

The officer gave Zhang Wei a hateful smile and was about to climb into an armored vehicle when—

Whoooosh—boom!

Zhang Wei blinked blankly. When he wiped his face with his palm, it came away covered in sticky blood.

The substance was unmistakably human blood, bright red without end. The officer’s body, already missing its entire upper half, rolled out of the armored vehicle.

Thud.

A suffocating silence descended. Zhang Wei was the first to regain his senses.

“Everyone, prepare for battle!”

“Monsters! Monsters have appeared!”

“Tank!”

“T-The regimental commander has been killed!”

The Hunters of the Public Security Armed Forces were the first to react to the shouts. The soldiers understood what was happening a moment later.

And waiting for them, already thrown into utter chaos by their commander’s sudden death, was an even more horrific death.

Whoooosh!

A single sound of air being split.

A streak of light fired at an invisible speed swept across the soldiers marching in orderly ranks.

Boom-boom-boom!

The streak of light burst dozens of people like balloons as it advanced, then finally pierced the armored vehicle moving under the protection of the infantry.

It broke through the vehicle’s hard outer shell and burrowed deep inside. The sight made Zhang Wei shout like a thunderclap.

“Everyone, get clear!”

But before his voice could reach them, the thunderous roar that erupted the next moment swallowed everything.

KABOOM!

The armored vehicle exploded in a red flash and black smoke. Its fragments became hundreds, thousands of blades, tearing into everything around them.

Soldiers and lower-ranking Hunters who failed to react in time alike fell like sheaves of straw. Countless bodies collapsed.

Those who were already dead did not move even an inch.

“……!”

“W-What the hell is this…?”

Zhang Wei shouted at the people frozen like statues.

“Spread out! Everyone, spread out! Get as far away from the tanks and armored vehicles as possible!”

But the soldiers, experiencing real combat for the first time in their lives, were frozen in place. And their opponent, who had yet to reveal itself, never failed to take advantage of the enemy’s confusion.

Whoooosh!

The sound of death rang out once again. But unlike before, there was more than one streak of light.

Boom! Boom-boom-boom!

“Aaaaargh!”

Flames erupted, and screams flooded the air.

The roughly twenty armored vehicles and tanks were disabled in the blink of an eye.

The three combat helicopters circling overhead also shattered into countless fragments and crashed to the ground.

Boom! Clatter, clatter.

Amid the horrific scene that could only be called a mountain of corpses and sea of blood, Zhang Wei felt a chill run down his spine.

*At least an A-rank monster. And not just one or two.*

Ironically, it was the most accurate judgment Zhang Wei would make that day.

Ssssss.

Between dark alleys and collapsed buildings, atop a still-burning building—

Ten figures appeared like black mist, staring down at the hundreds of surviving humans with blazing violet eyes.

A groan escaped Zhang Wei’s lips when he spotted the figures mounted on warhorses stripped down to their bones.

“…Death Knights.”

Once noble, they were knights of death corrupted by dark magic.

The very Death Knights that had vanished from sight after the Great Cataclysm along with the Lich had appeared. And there were no fewer than ten of them.

The first word that came to Zhang Wei’s mind was death.

*Is this where it ends?*

Death Knights were beings that had surpassed A-rank monsters.

A hundred Hunters and the military forces still remained, but Zhang Wei already knew.

They could not escape the net that had been spread around them.

But…

“I have no intention of dying quietly.”

That thought did not belong to Zhang Wei alone.

Unlike the soldiers, who were so terrified they could barely hold their guns properly, the Hunters of the Public Security Armed Forces raised their weapons with eyes full of resolve.

“You don’t have to do this.”

One of the platoon commanders answered Zhang Wei’s quiet words bluntly.

“And you do?”

“I’m sorry. I shouldn’t have brought you here.”

“No one brought us. We followed you. We’ve survived more than ten times thanks to you, Company Commander. It was about time we faced something like this at least once.”

He spoke as though it were nothing, but he could not hide the tremor in his voice.

Zhang Wei licked his parched lips as he stared at the ten Death Knights that remained perfectly still.

“Fight with everything you have, and make sure at least one of you survives. That’s all I have to say.”

A thunderous cheer erupted in place of an answer. The Hunters’ eyes, their fear driven away, shone like morning stars.

If they had wanted safe and prosperous lives, they could have chosen another path.

But they had chosen the Public Security Armed Forces over becoming bodyguards for wealthy entrepreneurs or mercenaries because of their honor and sense of responsibility as Hunters.

This was a battle they could never retreat from.

“Forward! Sons and daughters of the people, descendants of Zhonghua!”

Just as Zhang Wei roared with all his strength and was about to charge toward the nearest Death Knight—

Rumble-rumble-rumble!

It was almost instinctive.

A tremendous force accompanied the violent tremors. The surviving humans turned their heads, terror making every hair on their bodies stand on end.

Where countless eyes turned, a black knight was slowly crossing the ruined downtown area.

Red eyes flashed beneath a helmet pulled low. The breath of death poured from between its bloodless lips.

—Sar, Garosh.

A language of the demon realm that no one could understand.

But the next moment, Zhang Wei realized what the words meant.

*Kill them all.*

The ten Death Knights charging from every direction were reflected in Zhang Wei’s wide-open eyes.

Slice!

The massacre began.

* * *

Splash.

A horse’s bony hoof stepped into a pool of blood.

The Death Knights approached the black knight, who was gazing down at the corpse of Zhang Wei, the middle-aged Hunter who had resisted until the very end, and dropped to one knee.

—Lord. Awaiting your next command.

The next command.

After remaining silent for a moment, the black knight suddenly extended a hand.

Whoosh—slice!

A black streak of light, swung like a whip, cut through concrete and rebar.

The building collapsed at an angle. Inside the exposed space, humans were crouched together with their hands clamped tightly over their mouths.

“Jinjin. Honey. It’s okay, it’s okay…”

“Sniff… sob…”

“Dada?”

A human male and female. And…

A being so small and light that it was impossible to tell whether it was male or female.

Perhaps that was what they called a child.

*Child. Child?*

Where had he heard that word before?

The black knight pushed the question aside and extended his hand. The humans within sight had to be annihilated. That was the order he had received.

But—

—……?

For some reason, his hand would not move forward.

The creatures were clearly so weak that the snap of a finger would turn them into a handful of blood and make them disappear. And yet it was as if an invisible barrier surrounded them.

—What are you?

At the black knight’s eerie voice, the child wriggling in its parents’ arms suddenly burst into a wailing cry.

—This is…

The black knight abruptly lifted its head and looked into the distance before turning its horse around.

The Death Knights questioned their leader’s sudden movement.

—Lord?

—We’re leaving. Now. At once.

—Then we’ll take care of the humans—

—We’re leaving. Now. At once.

That was all.

The ten Death Knights knelt in salute, then spurred their horses after their leader.

Just before they vanished like mist, the black knight’s red eyes touched the three humans who had survived by a miracle, then moved away.

Whoooooosh.

A wind carrying the smell of blood swept through the ruins filled with corpses.

[^1]: *Guanxi* refers to a network of personal connections and favors, especially one useful in politics or business.
```
