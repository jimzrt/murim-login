<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0098.txt",
      "sha256": "e1ef5038a97ff357c351426ccd72689c7f351c7029af897bade2b8092d444ead",
      "bytes": 13770
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "798083d19c79a33f8abfc0e1890fedb3d2470010fd8528f4c734f52df28d1609",
      "bytes": 3019
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8c5e8b96be5f9aca3aea3f792b4623838a9f9dfb15b8e5d04288a0abbb919749",
      "bytes": 11955
    },
    {
      "path": "characters/Jin Hayeon.md",
      "sha256": "b1f865ed1c8901510029913859ac09a9f922114863f24d6502ae88c9bacaf04c",
      "bytes": 1449
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6dfa78ac864518a4bb0cbbe91bde6a4e01aa60ec93cfa4967c4a1863ae68f8af",
      "bytes": 23942
    },
    {
      "path": "characters/Kim Gwondong.md",
      "sha256": "7c9ddfc553359d219b6b165fba0b2ff03fa6075e58759097ddbeda3d8359d6c0",
      "bytes": 629
    },
    {
      "path": "characters/Kim Junsu.md",
      "sha256": "041fa5ed2bf4ca0782b8cb47658781c4d7fdf1870c0b7aef67d0ebfe6885d0ac",
      "bytes": 594
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4ea8a9c52f6b4e99a2f20956dcf0c77142bb1ae442b12074bb437b9c1c8d1c54",
      "bytes": 10832
    }
  ],
  "estimated_tokens": 15019
}
-->

# Durable State Update — Chapter 98

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 98. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 98. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 98,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 98,
    "continuity_sources": [98],
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
    "Sangdong Guild's Security Team is monitoring Jin Taekyung with its sole Familiar mage, Kim Junsu, and multiple C-rank stealth and tracking Hunters.",
    "Kim Junsu is a C-rank mental mage who uses Familiars and is suffering from exhaustion and anxiety about his hair loss.",
    "Kim Gwondong is a Level 42 C-rank Security Team Hunter assigned to surveillance and disguises himself as a friendly neighbor.",
    "The Security Team has been watching Taekyung for days and has installed eavesdropping-magic Equipment in nearby real-estate offices.",
    "The Security Team uses a black Level 2 Cat Familiar to track Taekyung after he leaves home.",
    "Taekyung detects the black kitten as a Familiar and recognizes Kim Gwondong's disguise, while continuing to keep his own suspicions concealed.",
    "The Security Team Leader is offended by the real-estate ajumma's old-bachelor insult, leaves for a sauna, and orders his subordinates to prepare a transcript and individual opinion statements.",
    "The surveillance team currently regards Taekyung's boastful conduct as the childish behavior of a newly reawakened C-rank Hunter and has become less tense while monitoring him.",
    "Taekyung learns of three properties traded within five days and five hundred meters of his home: Building 5, Unit 901; Building 4, Unit 302; and Building 3, Unit 202.",
    "Taekyung plans to scan the area and parking lot with Qi Sense while pretending to take a walk, then capture the watchers and learn their backer.",
    "The black kitten Familiar remains at its previous location, and Kim Gwondong reminds Taekyung that it is still waiting there."
  ],
  "continuity_sources": [
    97
  ],
  "open_questions": [
    "Why did Sangdong Guild's Guild Master issue a special warning about Taekyung?",
    "Who commissioned the surveillance operation and who is directing it?",
    "Which of the three recently traded properties, if any, is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Whether the Security Team's operation and Hong Woojin's investigation share the same commissioning chain remains unresolved.",
    "Whether the surveillance team has identified Taekyung's deliberate deception remains unresolved."
  ],
  "safe_through": 97,
  "temporary_decisions": [
    "Render 정신계 마법사 as mental mage and 보안팀 as Security Team.",
    "Use Kim Junsu, Kim Gwondong, Nabi, and Goyang for 김준수, 김권동, 나비, and 고양시.",
    "Render 개냥이 as dog-cat with an explanatory footnote.",
    "Use target, Familiar, Link, and eavesdropping-magic Equipment for 표적, 패밀리어, 링크, and 도청 마법 장비.",
    "Render 도청 마법 as wiretapping magic when referring to the magic itself.",
    "Render 월세 as monthly rent and 전세 as jeonse lease.",
    "Render 홀아비 냄새 as old-bachelor smell."
  ],
  "version": 1
}
```

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
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |

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
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 진하연    | **Jin Hayeon**    |
| 홍우진    | **Hong Woojin**   |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 귀가      | **your family**                                                 |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |

## Listed compact profiles

### Jin Hayeon.md

# Jin Hayeon (진하연)

- **Safe through:** Chapter 95
- **Aliases:** Hayeon; Taekyung’s younger sister
- **Role:** High-school senior preparing for the college entrance exam
- **Personality:** Sharp-tongued, academically gifted, impatient with Taekyung’s evasions, warmer beneath the teasing, and intensely fond of cats
- **Voice:** Bratty, fast, blunt sibling banter; turns brighter when discussing school and her interests
- **Relationships:** Taekyung’s younger sister; daughter of Taekyung’s mother

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 97
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Kim Gwondong.md

# Kim Gwondong (김권동)

- **Safe through:** Chapter 97
- **Aliases:** None
- **Role:** Level 42 C-rank Hunter in Sangdong Guild’s Security Team, specializing in surveillance and disguise.
- **Personality:** Cautious, observant, pragmatic, and cynical about his superior’s orders and accountability.
- **Voice:** Friendly and ordinary while acting as a neighbor; deferential aloud to his Team Leader and profane internally.
- **Relationships:** Works under the unnamed Security Team Leader and cooperates with Kim Junsu and the other surveillance Hunters.

### Kim Junsu.md

# Kim Junsu (김준수)

- **Safe through:** Chapter 97
- **Aliases:** None
- **Role:** C-rank Hunter in Sangdong Guild’s Security Team; the Guild’s sole Familiar mage and a rare mental mage.
- **Personality:** Exhausted, anxious about his worsening hair loss, dutiful, and privately profane about his workload.
- **Voice:** Polite and restrained aloud; internally self-pitying, sarcastic, and profane.
- **Relationships:** Works under the unnamed Security Team Leader alongside Kim Gwondong and other surveillance Hunters.

## Korean source

```text
＃98화



홍우진은 후회했다.

‘내 생각이 짧았구나.’

침입은 성공적이었다. 고양이 덕후인 표적의 여동생에게 접근, 애처로우면서도 반짝이는 눈망울로 마음을 사로잡았으니까. 다만 문제는…….

“우리 여름이는 뭘 먹고 이렇게 귀여워요? 응? 응응?”

미야옹.

“여름아, 왜 자꾸 문밖으로 나가려고 해. 여기서 언니랑 놀자.”

야옹.

“꺅, 너무 귀여워!”

하악! 하아아악!

“헉, 여름이 화났어? 미안해. 언니가 너무 만졌지? 알았어, 가만히 있을 테니까 침대 위에서 놀고 있어. 응?”

이 망할 여동생이라는 녀석이 도무지 밖으로 내보내 줄 생각을 안 한다는 거다. 덕분에 하루 반나절 이상을 진하연의 방에 갇혀 지내는 신세가 됐다.

‘차라리 개로 할걸.’

개였다면 지금처럼 쉽게 들어올 수는 없었겠지만 들어온 이후에 반 감금되어 있지는 않았을 것이다. 적어도 산책 정도는 시켜 줬을 테니까.

‘이대로는 죽도 밥도 안 된다.’

위기감에 휩싸인 홍우진은 탈출을 시도했다.

‘네가 이기나, 내가 이기나 보자!’

그렇게 독한 마음으로 시작했는데…….

벅, 벅벅벅벅.

“…….”

야옹. 야오오오옹.

“…….”

첫 번째 시도는 실패다. 괜히 방문도 박박 긁어 보고, 큰 소리로도 울어도 봤지만 진하연은 책상에 앉아 단 한 번도 반응하지 않았다.

이어폰도 끼지 않은 채 그저 매서운 눈빛과 손놀림으로 문제집을 풀어 가고 있을 뿐.

‘전국 상위 0.01%라더니.’

1차 조사 자료에서 봤다. 중학교 때부터 전교 1, 2등은 예사고 각종 경시 대회에서 입상한 경력이 수두룩했으니 잊기도 힘든 내역이다.

홍우진은 오늘에서야 그 이유를 알았다. 책상 앞에 앉은 그녀는 정말이지, 어마 무시한 집중력의 소유자였다.

‘이런 애가 마법사 하면 딱인데……가 아니고.’

그는 그 후로도 어떻게든 공부를 방해하려고 애썼다. 쉴 새 없이 발을 건드리고 애교를 부려 댔다.

하지만 진하연의 대응은 간단했다.

“언니 지금 공부 중이야. 방해하면 안 돼.”

의자에 발을 올려 책상다리로 앉아 버리고 나니 이 조그마한 몸으로는 결코 닿을 수 없게 되었다. 아기 고양이의 한계였다.

‘이번 작전은 실패다.’

공부 방해 작전이 실패로 돌아갔으니 별수 없이 최후의 카드를 꺼내야 한다. 인간의 존엄성에 큰 손상을 입겠지만 지금은 이것저것 가릴 때가 아니었다.

‘이것도 무시하나 보자.’

쉬이이이이.

새하얀 이불보가 노랗게 물든다. 본래 큰일과 작은 일은 한 번에 해결해야 하는 법. 두 가지 일을 동시에 끝마친 홍우진은 굳게 결심했다.

‘그래, 기왕 이렇게 된 거 확실하게 처리하자. 프로답게.’

데굴데굴.

패밀리어 마법을 시작한 지 5년. 이렇게까지 망가진 적은 이번이 처음이었다. 그는 끊임없이 자기 세뇌를 걸었다.

‘나는 프로다, 나는 프로다, 나는 프로다…….’

잠시 후, 뭔가 이상한 냄새를 맡은 진하연이 고개를 돌렸을 때는 모든 게 끝난 후였다.

미야옹.

대소변으로 물든 이불, 마찬가지로 오물로 범벅이 된 아기 고양이 한 마리.

“꺅, 여름아!”

깜짝 놀란 진하연이 신속하게 움직였다. 더러워진 이불을 걷고, 조심스럽게 고양이의 뒷덜미를 잡아 들어 올렸다.

“화장실 두고 여기서 싸면 어떡해. 우리 여름이 씻어야겠다.”

‘그래, 문으로 가라! 문!’

고대하던 순간이다. 비록 오물로 범벅이 된 채 스무 살도 안 된 여자애의 손에 대롱대롱 매달려 있지만 홍우진은 희열에 가득 찼다.

달칵.

열린다, 문이!

어제 이후로 보지 못했던 거실이 보인다!

미야옹! 미야오옹!

“이상하네. 얘가 왜 이렇게 좋아하는 것 같지?”

진하연이 갸우뚱하던 그때였다.

비밀번호를 입력하는 익숙한 기계음과 함께 현관문이 열렸다.

“다녀왔습니…… 뭐냐, 그건?”

“어디 다녀왔…… 그건 뭐야?”

남매는 서로를 황당한 시선으로 바라봤다. 정확히 말하면 각자의 손에 들린 생물체를.

야옹.

미야옹.

황당한 시선을 교환하는 것은 이쪽도 마찬가지였다.

‘저게 홍우진?’

‘저놈은 상동 길드의 아마추어?’

그리고 이어지는 생각.

‘쟤는 왜 온몸에 똥칠을 하고 있어?’

‘아, 시바.’

홍우진이 갖고 있던 마지막 인간의 존엄성이 와르르 무너지는 순간이었다.



* * *



“이불에다가 똥칠을 해 놨다고?”

“어. 잠깐 공부하는 사이에 실수했나 봐.”

실수는 개뿔, 다분히 의도적이다.

하연이가 방에만 두고 물고 빠니까 어떻게든 나오려고 머리 굴린 거지, 뭐.

미야옹…….

고양이, 아니 이제 두 마리니까 이름을 불러 줘야겠구나.

어쨌건 여름이의 힘없는 울음소리에 하연이가 걱정스러운 얼굴로 물었다.

“애가 아까부터 힘이 없어.”

“음, 그럴 수 있지.”

모르긴 몰라도 자괴감이 장난 아닐 거다.

몸에 똥칠한 채로 업계 동업자와 감시 표적을 동시에 맞닥트렸으니까.

“너무 걱정하지 마. 원래 고양이들은 몸에 물 닿는 거 싫어하잖아.”

“그래서 그런 건가? 아냐, 아까 씻길 땐 반항도 안 하고 얌전하던데.”

“아, 그래?”

“기분 탓인지는 모르겠는데…… 애가 좀 넋이 나간 느낌이야. 자기도 사고 친 걸 알아서 미안해하는 건가?”

우리 여름이, 현자 타임이 제대로 왔구나.

나는 웃음을 삼키며 말했다.

“그거야 모르지. 아무튼 너 이불 어쩌냐? 시트도 새로 갈아야 되겠네.”

“괜찮아. 사람이 한 것도 아니고 동물인데, 뭘.”

별생각 없이 던진 돌에 개구리가 맞아 죽는다더니.

지금이 딱 그 상황이다. 하연이의 한마디는 비수로 변해 누군가의 가슴에 꽂혔다.

움찔.

울음소리도 못 내고 작은 몸을 부르르 떠는 아기 고양이 한 마리. 반면 다른 한쪽은 신이 났다.

그릉, 그르릉.

기분 좋은 소리를 내며 내 다리에 연신 얼굴을 비벼 대는 검은 고양이를 하연이가 귀여워 죽겠다는 얼굴로 바라봤다.

“얘는 어디서 데려왔어?”

“아파트 단지 입구에서.”

“길고양이야?”

“그렇겠지. 혼자 있었으니까.”

“뭐? 그럼 엄마가 있을지도 모르잖아. 그래서 새끼 고양이는 하루 정도는 지켜보고 데려와야 해.”

“어떤 아저씨한테 들었는데, 어제부터 혼자 울고 있었다는데?”

“아, 그럼 엄마 없네.”

움찔!

골골거리던 애교가 딱 멎는다. 자신도 모르는 사이에 2킬을 달성한 하연이가 해맑게 웃었다.

“우쭈쭈. 너도 엄마가 없구나. 괜찮아, 오늘부터 언니가 엄마 해 줄게.”

“…….”

내 동생이지만 웃는 얼굴로 엿 먹이는 재주가 제법인데.

검은 고양이는 직업 정신과 패드립 사이에서 갈등하는 듯했지만 이내 현실을 받아들였다.

야옹.

어머니의 원수에게 애교를 부리는 모습이 처량하기까지 하다. 저런 게 바로 직장인의 애환이지.

지켜보고 있자니 문득 엄마에게 생각이 미쳤다.

“엄마는?”

“몰라, 중요한 약속 있다고 나가셨어.”

“약속?”

“응, 요즘 자주 나가셔.”

무슨 일이지?

근래 들어 엄마의 외출이 잦아졌다. 일을 관둔 후 어느 정도 여유가 생기니 스스로의 삶을 찾으시는 걸까?

‘그러고 보니 분위기가 이상하긴 했지.’

뭔가 할 말이 있는 듯한 얼굴로 앉아 계신다거나, 갑자기 말을 걸면 화들짝 놀란다거나. 확실히 엄마의 주변에 어떤 변화가 일어나고 있는 것은 분명해 보인다.

‘때가 되면 말씀해 주시겠지.’

내가 세상에서 가장 사랑하고 믿는 분이 바로 우리 엄마다. 언제나 그렇듯이 믿고 기다리는 수밖에.

물론 적절한 시기에 함께 대화를 나누고 이야기를 들어 드리는 것도 자식의 도리다.

“무슨 생각을 그렇게 해?”

“별것 아냐. 그나저나 너는 어디 안 나가냐?”

“뭐야, 꼭 어디 나가기를 바라는 말투네.”

“꼭 그런 건 아니고.”

“흠, 수상해. 여자 친구 데려오려는 건 아니지?”

“…….”

제발 데려올 여자 친구라도 있었으면 좋겠다.

생각이 고스란히 드러나는 내 표정에 하연이가 주춤했다.

“아, 미안.”

“……사과하지 마. 두 배로 비참해져.”

“진짜 미안해.”

“너 일부러 이러는 거지?”

“생각해 보니까 도서관에 책 반납해야 할 게 있네.”

방 안으로 뛰어가더니 가방을 들쳐 메고 나오는 속도가 광속이다. 쾅 소리와 함께 현관문이 닫히자 집 안이 조용해졌다.

‘솔로의 마음을 후벼 놓다니.’

가슴 한구석이 휑해졌지만 내가 원하던 무대가 드디어 만들어졌다.

가급적이면 가족이 없을 때 해결해야 될 문제니까.

미야옹.

야옹.

각기 검고 흰 두 마리의 고양이가 슬금슬금 다가와 주위를 맴돌기 시작했다. 초롱초롱한 눈망울, 쫑긋 선 귀.

나에 대한 정보를 건지고 싶어 안달이 난 패밀리어들을 뒤로하고 베란다로 나갔다.

가장 먼저 보이는 건 수백 대의 차량이 늘어선 주차장이다.

‘주차장은 클리어.’

귀가하기 전, 패밀리어를 품에 안고 아파트 단지를 한 바퀴 돌아 보았다. 남들 눈에는 날씨 좋은 날 산책하는 한량으로 보였겠지만 목적은 차량 확인이었다.

결과는 이상 무.

‘그럼 역시 집밖에 없지.’

이로써 감시자들이 최근 거래된 아파트를 아지트로 삼았음이 확인됐다. 나는 부동산에서 얻은 정보를 다시 한번 떠올렸다.

‘5동 901호. 4동 302호. 3동 202호.’

공교롭게도 세 곳 전부 우리 아파트를 중심으로 감싸는 형태로 자리해 있다. 창문으로도 동 입구를 내려다볼 수 있어 감시에 용이한 위치.

감시자들이 어느 곳에 있어도 이상하지 않다.

‘문제는 저 중 어디에 숨었냐는 건데…….’

발각을 우려해 마법 장비가 아닌 패밀리어를 붙일 정도로 조심성을 갖춘 놈들이다.

섣부르게 다가갔다가는 놓친다. 확실한 검거를 위해서는 그만큼 큼지막한 미끼를 던지는 수밖에 없다.

‘슬슬 시작해 볼까.’

촥, 촤르륵.

우선 집 안의 모든 커튼을 쳤다. 한낮임에도 불구하고 어둑해진 거실 중앙에서 주머니를 뒤적였다.

‘인벤토리 오픈. 마나 탐지 장비.’

동시에 손바닥의 절반만 한 쇳덩이가 손에 잡혔다.

이름 그대로 마나를 탐지할 수 있는 장비, 스토어에서 2천만 원이나 주고 산 물건이다.

‘다음 단계, 수색.’

탐지 장비를 들고 집 안을 꼼꼼히 훑었다. 내부에 아무런 마나가 감지되지 않는 걸 확인하고 스마트폰을 꺼내어 누군가에게 통화를 걸었다.

뚜, 뚜. 달칵.

통화 연결음과 함께 상대방이 전화를 받았다.

- 여보세요?

내가 대답했다.

“접니다, 진태경.”

그런 내 모습을 두 마리의 패밀리어가 숨도 쉬지 않고 지켜보고 있었다.



* * *



김준수는 눈을 뜸과 동시에 외쳤다.

“왔어요, 왔어!”

옹기종기 모여 앉아 소견서를 쓰고 있던 보안팀원들이 화들짝 놀랐다.

“뭐?”

“누가 와? 우리 팀장?”

“아니면 설마…….”

말꼬리를 흐린 팀원을 향해 김준수가 고개를 끄덕였다.

“표적이요. 이 자식 이거 구린내 장난 아닙니다.”

“진짜로?”

“네. 집 비자마자 커튼 칠 때부터 뭔가 쎄 했는데, 탐지 장비까지 사용해서 집 안 점검하더라고요.”

평범한 C급 헌터, 그것도 휴가 중인 놈이 할 만한 일이 아니다. 방 안의 모두가 침을 꿀꺽 삼켰다.

“그, 그래서?”

“폰 꺼내더니 전화부터 걸던데요.”

“전화? 누구한테?”

“그걸 모르겠어요.”

김준수가 미간을 찡그렸다.

“통화가 3분도 안 될 만큼 짧았던 것도 있지만, 호칭에 굉장히 주의한다는 게 느껴질 정도?”

“그 정도면 충분해. 일단 윗선에 보고해서 저놈 통화 기록 털어 보면 되니까.”

“그래, 더 나온 건 없고?”

“왜 없겠습니까. 그놈이 뭐라고 한 줄 아세요?”

크흠. 한차례 목을 가다듬은 그의 입에서 낮은 목소리가 흘러나왔다.

“계획은 차질 없이 진행 중입니다. 네, 네. 상동 길드 쪽에서는 아직 눈치 못 챘습니다. 물건은 잘 갖고 있습니다.”

듣고 있던 팀원들이 무릎을 탁 쳤다.

“이거네!”

“드디어 하나 건졌다.”

“와, 방금 살짝 소름 돋았어. 이거 무슨 비밀 요원이야?”

그때, 가만히 듣고 있던 김권동이 불쑥 입을 열었다.

“진수야, 방금 그 자식이 무슨 물건 갖고 있다고 하지 않았냐?”

“좋은 지적입니다.”

김진수가 의미심장하게 웃었다.

“그놈, USB를 갖고 있어요.”
```

## Final English reading copy

```markdown
# Chapter 98

Hong Woojin regretted it.

*I didn't think this through.*

The intrusion itself had gone perfectly. He had approached the target’s cat-loving younger sister and won her heart with a pair of pitiful yet sparkling eyes.

The problem was…

“What does our Yeoreum eat to be this cute? Hmm? Hmm-hmm?”

*Meow.*

“Yeoreum, why do you keep trying to get out the door? Stay here and play with your big sis.”

*Meow.*

“Eek, you’re so cute!”

*Hiss! Hissssss!*

“Oh no, is Yeoreum mad? I’m sorry. Did Sis touch you too much? Okay, I’ll stay still, so play on the bed, all right?”

This damn younger sister had absolutely no intention of letting him outside. Thanks to her, he had spent more than a day and a half trapped in Jin Hayeon’s room.

*I should’ve gone with a dog.*

If he had been a dog, getting inside wouldn’t have been this easy. But once he was in, he wouldn’t have been practically held captive, either. At the very least, they would have taken him out for walks.

*This gets me nowhere.*

Swept up by a sense of crisis, Hong Woojin attempted to escape.

*Let’s see who wins—you or me!*

He had begun with that fierce resolve, but then…

Scritch, scritch-scritch-scritch.

“…”

*Meow. Myaaaaaow.*

“…”

His first attempt was a failure. He scratched desperately at the door and even tried crying as loudly as he could, but Jin Hayeon didn’t react even once.

Without even putting on earphones, she simply continued solving problems with a fierce look in her eyes and swift movements of her hands.

*So this is what it means to be in the top 0.01 percent nationwide.*

He had seen it in the initial investigation report. Ever since middle school, she had routinely ranked first or second in her entire school and had earned countless awards in various academic competitions. It was hard to forget a record like that.

Only today did Hong Woojin understand why.

Sitting in front of her desk, she possessed truly terrifying powers of concentration.

*Someone like this would make the perfect mage… No, that’s not the point.*

He continued trying to disrupt her studies somehow. He pawed at her feet without pause and kept acting cute.

But Jin Hayeon’s response was simple.

“Big sis is studying right now. Don’t bother me.”

She pulled her feet up onto the chair and sat cross-legged, putting them completely out of reach of his tiny body.

That was the limit of being a kitten.

*This operation has failed.*

Since his plan to disrupt her studies had gone up in smoke, he had no choice but to bring out his final card. It would deal a serious blow to his human dignity, but this was no time to be picky.

*Let’s see if you ignore this, too.*

Sssssssss.

The pristine white duvet turned yellow.

When nature called, it was best to take care of both kinds of business at once. Having finished both simultaneously, Hong Woojin made a solemn decision.

*Fine. Since things have come to this, I might as well take care of it properly. Like a professional.*

He rolled over and over.

It had been five years since he started using Familiar magic. This was the first time he had ever fallen this far.

He kept hypnotizing himself.

*I’m a professional. I’m a professional. I’m a professional…*

A little while later, Jin Hayeon noticed a strange smell and turned around.

By then, everything was over.

*Meow.*

A duvet stained with urine and feces, and a kitten covered in filth.

“Eek, Yeoreum!”

Jin Hayeon was startled and moved quickly. She pulled off the dirty duvet, then carefully grabbed the kitten by the scruff of its neck and lifted it up.

“What are you doing going to the bathroom here when your litter box is right there? We need to wash our Yeoreum.”

*Yes, go to the door! The door!*

This was the moment he had been waiting for.

Even though he was covered in filth and dangling from the hand of a girl who wasn’t even twenty, Hong Woojin was filled with joy.

Click.

The door was opening!

The living room he hadn’t seen since yesterday came into view!

*Meow! Myaaaow!*

“That’s strange. Why does it look so happy?”

Jin Hayeon tilted her head.

That was when the front door opened with the familiar electronic tones of someone entering the passcode.

“I’m ho—… What is that?”

“Where have you been—… What’s that?”

The siblings stared at each other in bewilderment.

More precisely, they stared at the creatures in each other’s hands.

*Meow.*

*Myaow.*

The two cats exchanged equally bewildered looks.

*That’s Hong Woojin?*

*That guy is the Sangdong Guild’s amateur?*

And then came the next thought.

*Why is he covered in shit from head to toe?*

*Ah, fuck.*

It was the moment the last shred of Hong Woojin’s human dignity collapsed.

* * *

“You smeared poop all over the duvet?”

“Yeah. I guess he had an accident while I was studying for a bit.”

*An accident, my ass.*

Since Hayeon had kept him in her room, petting and cuddling him nonstop, he had wracked his brain for a way to get out.

*Myaow…*

A cat.

No, there were two of them now, so I supposed I should call them by their names.

Whatever the case, Hayeon asked worriedly at the sound of Yeoreum’s feeble cry.

“He’s been looking weak for a while.”

“Hmm. That can happen.”

I couldn’t say for sure, but his self-loathing had to be something else.

He had run into both a fellow professional and his surveillance target while covered in shit.

“Don’t worry too much. Cats normally hate getting water on their bodies.”

“Is that why? No, he didn’t even resist when I washed him earlier. He was completely docile.”

“Oh, really?”

“I don’t know if it’s just my imagination, but he seems kind of out of it. Maybe he knows he made a mess and feels sorry?”

*Our Yeoreum had a serious case of post-nut clarity.*

I swallowed my laughter and said, “Who knows? Anyway, what are you going to do about the duvet? You’ll have to change the sheets, too.”

“It’s fine. It was an animal, not a person. What’s the big deal?”

They say a frog can die from a stone thrown without a second thought.

That was exactly what had happened here. Hayeon’s offhand remark turned into a blade and lodged itself in someone’s chest.

The kitten trembled violently in silence, unable to even cry out.

Meanwhile, the other one was having a wonderful time.

*Purr. Prrrr.*

Hayeon gazed at the black cat with a face full of adoration as it repeatedly rubbed its face against my leg, making happy noises.

“Where did you bring him from?”

“The entrance to the apartment complex.”

“Is he a stray?”

“I guess so. He was alone.”

“What? Then he might have a mother. You’re supposed to watch a kitten for about a day before bringing it home.”

“Some man told me he’d been crying alone since yesterday.”

“Oh, then he doesn’t have a mother.”

The black cat flinched.

Its purring and attempts to act cute stopped dead. Without realizing it, Hayeon had scored two kills, and she smiled brightly.

“There, there. You don’t have a mother, either. It’s okay. From today onward, Sis will be your mommy.”

“…”

For my little sister, she certainly had a talent for screwing people over with a smile.

The black cat seemed torn between professional duty and the cheap shot at his mom, but soon accepted reality.

*Meow.*

The sight of it acting cute for its mother’s enemy was downright pitiful.

*That’s the hardship of being a working stiff.*

Watching them, I suddenly thought of Mom.

“Where’s Mom?”

“I don’t know. She went out because she had an important appointment.”

“An appointment?”

“Yeah. She’s been going out a lot lately.”

*What’s going on?*

Mom had been leaving the house frequently these days. Now that she had some free time after quitting her job, was she finally looking for a life of her own?

*Come to think of it, she had been acting strange.*

Sometimes she would sit there with an expression that looked as though she had something to say. Other times, she would jump whenever I suddenly spoke to her.

Something had definitely changed around Mom.

*She’ll tell me when the time is right.*

The person I loved and trusted most in this world was my mother. Just as always, all I could do was trust her and wait.

Of course, listening to her and talking things over at the right time was also a child’s duty.

“What are you thinking about so hard?”

“It’s nothing. By the way, aren’t you going out?”

“What, you sound like you want me to leave.”

“Not exactly.”

“Hmm. Suspicious. You’re not planning to bring a girlfriend over, are you?”

“…”

*I wish I had a girlfriend to bring over.*

My expression must have revealed my thoughts, because Hayeon hesitated.

“Ah, I’m sorry.”

“Don’t apologize. It makes me twice as pathetic.”

“I’m really sorry.”

“You’re doing this on purpose, aren’t you?”

“Come to think of it, I have some books to return to the library.”

She sprinted into her room, threw on her backpack, and came back out at the speed of light.

The front door slammed shut, and the house fell silent.

*She really went and gouged out a single man’s heart.*

A corner of my chest felt hollow, but the stage I had been waiting for had finally been set.

This was a problem I needed to deal with while my family was out of the house, if possible.

*Myaow.*

*Meow.*

Two cats, one black and one white, began creeping toward me and circling around.

Bright eyes. Perked-up ears.

I left the Familiars, who were dying to learn more about me, behind and stepped onto the balcony.

The first thing I saw was the parking lot, where hundreds of cars were lined up.

*The parking lot is clear.*

Before returning home, I had carried the Familiar in my arms and taken a lap around the apartment complex. To everyone else, I probably looked like an idler out for a walk on a pleasant day.

My real purpose had been to check the vehicles.

The result was nothing suspicious.

*Then it has to be one of those houses.*

That confirmed the watchers had made one of the recently traded apartments their base. I recalled the information I had obtained from the real-estate office once more.

*Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.*

Coincidentally, all three were positioned around our apartment, forming a sort of ring. They were ideal for surveillance, since their windows offered a view of the entrances to the buildings.

It wouldn’t be strange for the watchers to be in any one of them.

*The question is which one they’re hiding in…*

They were cautious enough to use a Familiar instead of magical Equipment to avoid being discovered.

If I approached recklessly, I would lose them. To make a definite capture, I had no choice but to throw out equally substantial bait.

*I think it’s time to begin.*

Swish. Rustle.

First, I drew all the curtains in the house. Even though it was the middle of the day, the living room had grown dim. I reached into my pocket.

*Inventory open. Mana-detection Equipment.*

At the same time, my hand closed around a lump of metal about half the size of my palm.

As its name suggested, it was Equipment that could detect mana. I had paid twenty million won for it at the Store.

*Next step: search.*

I carefully swept through the house with the detection Equipment. After confirming that no mana was being detected inside, I took out my smartphone and called someone.

Beep. Beep. Click.

The other person answered as the call connected.

—Hello?

I replied.

“It’s me, Jin Taekyung.”

The two Familiars watched me without even seeming to breathe.

* * *

The moment Kim Junsu opened his eyes, he shouted.

“He’s here! He’s here!”

The Security Team members, who had been sitting close together and writing their assessments, jumped in surprise.

“What?”

“Who’s here? Our Team Leader?”

“Or could it be…”

Kim Junsu nodded at the team member who had let his voice trail off.

“The target. This guy reeks to high heaven.”

“Seriously?”

“Yes. I got a bad feeling when he drew all the curtains as soon as the house was empty, and then he even used detection Equipment to inspect the inside.”

That wasn’t something an ordinary C-rank Hunter, especially one on vacation, would do.

Everyone in the room swallowed hard.

“Th-then?”

“He pulled out his phone and made a call.”

“A call? To whom?”

“I don’t know.”

Kim Junsu furrowed his brow.

“The call was so short that it didn’t even last three minutes. But more than that, I could tell he was being extremely careful about how he addressed the other person.”

“That’s enough. We’ll report it up the chain and pull that bastard’s call records.”

“Right. And there was nothing else?”

“How could there be nothing else? Do you know what he said?”

He cleared his throat once. Then a low voice came from his mouth.

“‘The plan is proceeding without a hitch. Yes, yes. The Sangdong Guild hasn’t noticed anything yet. I have the item with me.’”

The team members listening slapped their knees.

“This is it!”

“We finally got something!”

“Wow, I just got chills. What is he, some kind of secret agent?”

At that moment, Kim Gwondong, who had been listening quietly, suddenly spoke.

“Junsu, didn’t that bastard say he had an item?”

“Good observation.”

Kim Junsu smiled meaningfully.

“That guy has a USB.”
```
