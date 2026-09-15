<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0102.txt",
      "sha256": "0c8271fc281e4654d4192135976e21d40246bce9c9390b734f5e739ecfa01c8d",
      "bytes": 13731
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5f6bb2e5f7462130b6007c824722959c74abda1cf692d4764704ed4971083467",
      "bytes": 2723
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "72f6ae6208d32d5a6714fdc9b5c9c6da04ec60c19e5cbdd5987344876055b4b0",
      "bytes": 12769
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b51a9e06064c81b0c3cab69af538be34ed271f985b5948a2a8c378b8a73b8c7d",
      "bytes": 23943
    },
    {
      "path": "characters/Seong Jinho.md",
      "sha256": "4c111d4dc25fe92689b2b1f0fefbda46fb2159b55fc6f02b3849b51c941a26e4",
      "bytes": 2028
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ec9aeaebc9528c2083a75bef017a64eda80186f012d0ec5dceb8190aab4fc9c9",
      "bytes": 12661
    }
  ],
  "estimated_tokens": 15440
}
-->

# Durable State Update — Chapter 102

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 102. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 102. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 102,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 102,
    "continuity_sources": [102],
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
    "Sangdong Guild's Security Team was assigned to surveil Jin Taekyung under Im Chunsoo's direction.",
    "Choi Byungil led the failed operation against Taekyung and was defeated alongside the other five field Hunters.",
    "Kim Junsu is the Security Team's sole Familiar mage and revealed the operation's information when Taekyung threatened his remaining hair.",
    "Hong Woojin was a B-rank Familiar mage hired from outside by Team Leader 1.",
    "Taekyung seized the Security Team's supplies, treated the wounded Hunters, and held them until Team Leader 1 released them.",
    "Im Chunsoo initiated the investigation after Im Changsoo was extorted for a hundred million won.",
    "Seong Jinho is Taekyung's thirty-year-old civilian goshiwon manager and sworn-brother-like friend in Bucheon.",
    "Im Chunsoo is a Level 75 A-rank ice mage and Guild Master of Sangdong Guild.",
    "Im Chunsoo attacked Taekyung with roughly a dozen ice spikes after inviting him to walk, and Taekyung stopped them with Fire Wall.",
    "Kim Hwajong is a Level 80 mage and former Class 3 Hunter Training Center instructor known as Butler Kim.",
    "Kim Hwajong trained Im Chunsoo, who was a Class 25 trainee assigned to the 28th Regiment, First Battalion, Second Company.",
    "The property being used as the surveillance base remains unidentified.",
    "The reason Kim Hwajong arrived at the confrontation remains unknown.",
    "Team Leader 1 assesses Taekyung as a top-tier B-rank or A-rank Hunter.",
    "The Security Team faces written disciplinary action, a pay cut, and possible dismissal for the failed assault.",
    "Taekyung returned home with Kim Hwajong and deferred their proposed exchange of stories."
  ],
  "continuity_sources": [
    100,
    101
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation remains unknown.",
    "Why Kim Hwajong, despite his former instructor status and exceptional ability, now works as a butler remains unexplained.",
    "What final disciplinary action will be taken against the Security Team remains unknown."
  ],
  "safe_through": 101,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술.",
    "Keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you while preserving his blunt senior voice.",
    "Render 김화종's 춘수 as Chunsoo.",
    "Render 교관님 as Instructor.",
    "Render 1번 훈련생 as Trainee Number One."
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
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |

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
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 생도     | **cadet**                                    |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 로그인              | **Login**                      |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 성진호 | **Seong Jinho** |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 101
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Seong Jinho.md

# Seong Jinho (성진호)

- **Safe through:** Chapter 100
- **Aliases:** Jinho; Mr. Seong Jinho
- **Role:** Manager of Hope Goshiwon; thirty-year-old exam candidate; civilian and Taekyung’s older friend
- **Personality:** Knowledgeable about IT, shamelessly blunt, melodramatic when threatened, and a heavy drinker
- **Voice:** Casual and teasing; invokes laws and hierarchy for comic effect; speaks informally to Taekyung while demanding respect as his older brother
- **Relationships:** Three years older than Jin Taekyung; treats him as a younger brother and drinking companion

## Korean source

```text
＃102화



사람마다 전문 분야가 다르기 마련이다.

게이트에서의 포메이션과 위기 상황이 닥쳤을 때 취해야 할 행동, 몬스터들의 약점 등을 달달 꿰고 있는 내가 법 관련 사항에서는 문외한인 것도 같은 맥락이었다.

“고생하셨습니다.”

“법무사님도요.”

각진 뿔테 안경을 쓴 이 남자는 내게 부동산 매매를 위임받은 법무사다. 맞은편에선 집주인과 공인중개사 아저씨가 인사를 나누며 막 자리에서 일어나고 있었다.

“계약 축하해요. 젊은 분이 성공하셨네.”

“아, 네. 감사합니다.”

집주인과 악수를 나누며 그제야 새로운 사실을 깨달았다.

‘이젠 내 집이구나.’

그리고 우리 가족의 집이다. 자그마치 11년 만에 되찾은.



* * *



좁은 방 안을 돌아봤다.

오래전 스프링이 나간 침대. 몇 벌 들어가지도 않는 작은 옷장과 군데군데 칠이 벗겨진 책상 하나. 그 위에 놓인 소형 TV.

두고 가야 할 것을 제외하고 옷이며 자질구레한 물건들을 주워 담으니 종이 박스 하나를 꽉 채웠다.

‘겨우 박스 하나.’

지난 7년이 그 안에 담겨 있다. 어쩐지 먹먹한 심정이 되어 하염없이 방을 둘러보고 있던 그때였다.

“가냐?”

굳이 돌아보지 않아도 알 수 있다.

내 7년에서 빼놓을 수 없는 사람이니까.

“응.”

“집은?”

“구했으니까 나가지.”

“새끼, 빠르네. 가족들은 이미 새집으로 이사했고?”

“아니. 아직까지는 비밀이야. 내가 먼저 들어가서 살다가 동생 수능 끝나면 알려 주려고.”

“하긴, 한창 중요한 시기니까.”

“응. 그 전에 리모델링도 해야 하고.”

잠깐 침묵이 흘렀다. 우리 둘은 굳이 대화를 나누지 않아도 편안한 사이, 눈빛만으로도 서로의 마음을 읽을 수 있는 사이지만 지금은 무슨 말을 해야 할지 모르겠다.

“형.”

“야, 야. 됐어. 분위기 잡지 마.”

진호 형이 내 등을 세게 두드렸다.

“무슨 전학 가는 초등학생도 아니고. 너 이사 가면 내 얼굴 안 볼 거냐?”

“봐야지. 꼭 봐야지.”

“그럼 됐어. 어차피 나도 오늘 중으로 짐 뺀다.”

“형도?”

“지난번에 말했잖아. 기억 안 나냐?”

“아, 그랬었지.”

몇 년씩이나 동고동락한 진호 형만 고시원에 두고 가는 게 마음에 걸렸는데, 이제야 한결 편해진다.

“형은 어디로 이사 가는데?”

“그냥 뭐 아는 사람 집에 얹혀살게 됐어. 너 이번에 산 집이 어디 있다고 했지?”

“고양시. 여기서 30분 거리라 그렇게 멀진 않아.”

“고양시?”

진호 형이 눈을 크게 떴다.

“나도 그 근처야, 인마!”

“어? 진짜?”

뜻밖의 이야기에 내심 반가웠다. 이제는 하루라도 안 보면 섭섭한 얼굴이다. 사는 곳이 가까우면 앞으로도 자주 만날 수 있겠지.

“형, 그럼 정확한 주소가 어디…….”

막 주소를 물어보려던 찰나, 주머니에 넣어 둔 스마트폰이 울렸다. 전화를 받으니 수화기 너머로 걸걸한 목소리가 흘러나온다.

- 어, 진태경 씨 맞죠? 지금 고시원 앞이에요.

“아, 예. 기사님.”

미리 불러 둔 개인 이삿짐 기사다. 흘끗 창문 밖을 바라보니 고시원 앞에서 기다리고 있는 파란색 용달차 한 대가 보였다.

- 짐 많아요? 무거운 거면 제가 도와드리고.

“아닙니다. 제가 들고 갈게요.”

짐이라고 해 봤자 두 개뿐이다.

소소한 물건들을 챙겨 넣은 종이 박스, 그리고…….

‘캡슐.’

로그아웃 기능이 활성화된 지금은 굳이 캡슐을 사용하지 않아도 무림과 현대를 넘나들 수 있다.

이제는 공간만 차지하는 애물단지가 됐지만 내게는 그 어떤 것보다 특별한 의미가 있었다. 짐이 별로 없는데도 용달차를 부른 것 역시 다 이거 때문이다.

‘이 캡슐이 아니었다면 어떻게 됐을까.’

천천히 캡슐 표면을 쓰다듬었다. 손을 통해 전해지는 금속의 차가움과 거칠거칠한 촉감.

이 낡은 캡슐 하나가 내 인생을 송두리째 바꿨다.

아, 맞다. 거기에 큰 역할을 해 준 사람도 있었지.

“진호 형.”

“응?”

어리둥절한 표정을 보고 있자니 실소가 절로 나온다.

그날, 진호 형이 술에 떡이 되지 않았더라면 내가 캡슐에 들어갈 일도 없었을 것이다.

“아냐, 아무것도.”

“싱겁기는. 그나저나 너 이제 가 봐야 하는 거 아니냐? 밖에 트럭 서 있던데.”

“어. 그런 김에 거기 박스 좀 들어 주라. 난 캡슐 들어야 해서 손이 부족해.”

“으, 응?”

“뭐야, 그 반응은? 이사 가는 동생을 위해서 박스 하나 못 들어 줘?”

“그게 아니고…… 어우, 생각해 보니까 나도 짐 싸야 되네. 귀찮아도 그냥 한 번 왔다 갔다 해라. 그럼 수고!”

“…….”

미꾸라지처럼 빠져나가는 것 보소. 나는 슬금슬금 멀어지는 진호 형의 뒷모습을 바라보다 결국 박스를 집어 들었다.

기다림에 지친 이삿짐 아저씨의 클랙슨 소리가 귀를 때린다.

빵빵!

“예, 지금 내려가요!”



* * *



“헌터신가 봐요?”

계속 나를 흘끗거리던 이삿짐 아저씨가 말을 던졌다. 박스와 캡슐을 실은 용달차는 내비게이션의 안내에 따라 새로운 집을 향해 달리고 있었다.

“어떻게 아셨어요?”

“그거야 보면 딱 알죠. 나도 예전에는 헌터였거든. F급.”

“어, 정말요?”

“아마 내가 손님보다 훈련소 기수로는 선배일걸? 아, 꼰대짓 하려는 건 아니에요. 딱 한 달 만에 때려치우고 자격증 반납한 놈이 그러는 것도 우습잖아.”

아저씨가 넋두리처럼 말을 이었다.

“헌터 훈련소 때는 할 만했어요. F급이지만 헌터가 된다는 자부심도 있었고. 그런데 수료 후에 길드 들어가자마자 사고가 터진 거지.”

게이트에서 사고가 터졌다는 말은 사망과 동의어다.

설령 팔다리가 날아가도 돈만 있다면 회복할 수 있는 세상이니까. 헌터들끼리는 그 정도를 사고라고 말하진 않는다.

“같이 입사한 훈련소 동기 녀석이었는데…… 어어, 하는 사이에 끌려가더니 그렇게 죽었어. 무슨 수를 써서라도 쫓아가서 구했어야 했는데 차마 발이 안 떨어지더라고. 그 녀석 장례식 마치고 은퇴 신청했지. 나 같은 놈은 레이드 뛰면 안 되니까.”

그는 애써 덤덤한 척하려 했지만 잘게 떨리는 목소리까지 감추지는 못했다.

“이거 헌터 손님 앞에서 너무 재수 없는 소리를 했네. 이게 뭐 좋은 얘기라고. 미안합니다.”

“별말씀을요.”

아저씨의 심정이 충분히 이해가 갔다.

나도 비슷한 경험이 있었으니까. 가족에 대한 책임감이 없었다면, 옆에서 위로해 준 진호 형이 없었다면 2년 전 그때 은퇴했을지도 모른다.

‘그럼 내 인생도 크게 달라졌겠지.’

헌터는 치열한 직업이다. 언론에서는 인류의 수호자요, 방패라며 치켜세워 주지만 늘 죽음을 옆에 끼고 살아간다.

- 50m 앞에서 우회전입니다.

내비게이션의 안내 음성에 아저씨가 멈칫하더니 중얼거렸다.

“어, 그러고 보니까 여기 안전 구역이네.”

“맞으니까 쭉 가 주세요.”

“아, 예.”

용달차는 얼마 지나지 않아 목적지에 도착했다.

푸른색 지붕의 2층짜리 단독주택. 너무 높지 않은 돌담과 잔디가 깔린 마당이 보인다. 이 집을 처음 봤던 며칠 전과는 또 느낌이 달랐다.

‘우리 집이라 그런 거겠지.’

우리 집.

곱씹을수록 기분 좋은 말이다. 물론 집이 워낙 예뻐서 그런 것도 있겠지만.

“이야…… 집 좋네.”

운전석에서 내린 아저씨가 혀를 내둘렀다. 다른 사람의 입에서 나오는 소리는 더 달콤하게 들리는 법. 참으려고 해도 자꾸 입꼬리가 올라간다.

“잘나가는 헌터인가 봐요. 내 꿈이 이런 집에서 사는 거였는데.”

“저도요.”

“소원 성취 하셨네. 좋으시겠어.”

당연히 좋아 죽지.

연신 감탄사를 터트리며 돌담도 만져 보고, 잔디밭도 바라보던 그가 물었다.

“잠깐 들어가서 구경해 봐도 될까요? 캡슐도 옮겨 드릴 겸.”

“네, 그러세요.”

의도치 않게 새집의 첫 손님이 된 이삿짐 아저씨가 짐칸으로 올라갔다. 캡슐을 옮기기 위해서다.

“그런데 그거 무게가 꽤 나갈 텐데.”

“괜찮아요. 저도 많이 옮겨 봐서 알아요. 게임 캡슐 무게야 거기서 거긴데요 뭘.”

“아니, 진짜 무거울 건데.”

아까 직접 들어 봐서 안다. 근력 스탯이 세 자리가 넘어가는 나한테도 적당히 묵직한 정도였는데 저 아저씨라면 더더욱 얘기가 다르다.

“사장님, 그냥 제가 옮길게요.”

캡슐을 끌어안은 그가 씩 웃었다.

“에헤이. 너무 무시하신다. 내가 그래도 왕년에 헌터였는데 겨우 이 정도로…… 끄응!”

“오오.”

역시 전직 헌터. 한 번에 들긴 들었다.

약간 변한 게 있다면 아저씨의 얼굴에서 웃음이 사라졌다는 것 정도?

“먼저 가서 문 열어요. 빨리!”

긴박한 목소리에 후다닥 달려가 대문과 현관문을 열어젖혔다. 이게 뭐라고 나까지 긴장되는지 모르겠다.

“그냥 제가 들…….”

“비켯!”

“아, 네.”

경보에 버금가는 속도로 거실에 들어간 그가 비명처럼 외쳤다.

“어느 방!”

“캡슐은 2층…….”

“뭣이?”

“……에 놓으려고 했는데 그냥 가까운 방에 놔 주세요.”

다행히 방문은 열려 있었다. 쿵, 소리와 함께 캡슐을 내려놓은 아저씨가 숨을 헐떡였다.

“이거, 왜, 이렇게, 허억. 무거워요?”

“…….”

내가 무겁다고 말해 주지 않았나?



* * *



이삿짐 아저씨가 떠나자마자 거실 소파에 털썩 걸터앉았다.

한 번에 잔금을 지급하는 조건으로 전 주인에게 양도받은 가구 중 하나다.

‘몇 달 동안은 혼자 살아야 하니까.’

가족들에게는 다시 부천으로 돌아간다고 말해 둔 상태.

하연이의 수능 전까지는 이곳에서 먹고 자며 출퇴근을 할 작정이다.

‘집 리모델링도 하고, 차도 사고. 아, 어차피 차는 길드에서 지원해 준다고 했으니 면허부터 따야겠구나.’

그밖에도 할 일이 태산이다. 그러나 지치기는커녕 힘이 솟았다. 전에는 하고 싶어도 못 했던 일들이니까.

게이트와 고시원을 오가며 고생만 하던 게 불과 몇 달 전인데, 참 많은 게 바뀌었다.

‘많이 컸다, 진태경.’

문득 생각나는 한 사람이 있다.

적지 않은 나이에도 늘 소년처럼 웃던 사람. 아내에게, 자식들에게 최선을 다하며 친구처럼 다가와 주었던 그가 떠오른다.

‘아버지, 나 집 샀어요. 예전에 우리가 살던 곳은 이미 없더라고. 그래도 이 정도면 잘한 거 맞죠?’

아이처럼 자랑하고 싶어도 칭찬해 줄 사람은 이미 오래전에 떠났다. 내가 할 수 있는 거라곤 마음속으로 닿지 않을 말을 되뇌는 것뿐이었다.

그렇게 시간이 얼마나 흘렀을까?

정신을 차려 보니 벌써 오후 여덟 시. 여름철의 해가 서서히 저물고 있었다.

‘휴가 마지막 날이 이렇게 끝나네.’

장장 일주일의 휴가. 상동 길드와 엮여 소란스럽기도 했지만 헌터 생활을 시작한 이래 처음으로 누리는 최고의 휴식이었다.

이제는 다시 일상으로 돌아가야 할 시간이다.

‘정확히 열두 시간 후에 말이지.’

앉아 있던 소파에 반듯이 누웠다. 캡슐에 들어갈까 하는 생각도 들었지만 이내 지워 버렸다.

11년 만에 돌아온 집이다. 이번만큼은 후덥지근한 캡슐 안이 아니라 우리 집 거실에서 깨어나고 싶었다.

‘로그인(Login).’

내 부름에 시스템이 응답한다.

띠링.



[무림]에 접속하시겠습니까?

Y   /   N



물론 내 대답은 예스다.



* * *



진태경이 의식을 잃은 지 한참 후, 현관문 옆 방 안에서는 누구도 예상 못 한 일이 벌어지고 있었다.

치이이익.

마치 거대한 알처럼 보이는 금속 물체, 캡슐의 문이 천천히 열리기 시작한 것이다.

가장 먼저 드러난 것은 두 발이었다.

종아리까지 덮는 긴 스포츠 양말에 프린팅된 붉은 글씨.



희망 고시원 조기축구회



이어 반쯤 말아 올린 추리닝 바지를 지나 희고 마른 양손까지 드러났다. 성서라도 되는 것처럼 꼭 붙잡고 있는 책 표지가 창밖으로 흘러들어온 노을빛을 받아 번쩍 빛난다.



행정고시 완전 정복



그리고 마침내 드러나는 그의 얼굴.

장장 몇 시간의 고통을 인내한 그는 사도세자처럼 초췌했으나 알을 깨고 태어난 박혁거세처럼 후련해 보였다.

바짝 마른 입술 사이로 메마른 음성이 새어 나온다.

“이곳이 나의 새로운 보금자리인가…….”

넓은 방을 바라보는 성진호의 입가에 흐뭇한 웃음이 맺혔다.
```

## Final English reading copy

```markdown
# Chapter 102

Everyone has their own area of expertise.

I knew the formations used at Gates, what to do when a crisis struck, and the weaknesses of various monsters like the back of my hand. My being clueless about legal matters was simply another example of everyone having their own specialty.

“Thank you for your hard work.”

“You too.”

The man in the angular horn-rimmed glasses was the legal scrivener I had hired to handle the real-estate transaction. Across from me, the homeowner and the licensed realtor were exchanging farewells and getting to their feet.

“Congratulations on the contract. A young man making it big.”

“Ah, yes. Thank you.”

As I shook hands with the homeowner, I realized something for the first time.

*This is my house now.*

And it was my family’s house.

A home we had reclaimed after no less than eleven years.



* * *



I looked around the cramped room.

The bed, whose springs had broken long ago. A small wardrobe that could barely hold a few outfits. A desk with its paint peeling off in places. A small TV sitting on top of it.

After packing up my clothes and assorted belongings, excluding the things I had to leave behind, I filled one cardboard box.

*Just one box.*

The past seven years were contained inside it. I was staring around the room with a strange tightness in my chest when a voice came from behind me.

“You leaving?”

I knew who it was without turning around.

He was someone I couldn’t leave out of my seven years.

“Yeah.”

“What about the house?”

“I found one, so I’m moving out.”

“Bastard, that was fast. Has your family already moved into the new place?”

“No. It’s still a secret. I’m planning to move in first and tell them after my sister finishes her college entrance exam.”

“Fair enough. She’s at an important stage.”

“Yeah. I need to remodel the place first, too.”

A brief silence followed. We were comfortable enough not to need conversation, the kind of people who could read each other’s thoughts from a look alone. But right now, neither of us seemed to know what to say.

“Hyung.”

“Hey, hey. Don’t set the mood.”

Jinho hyung slapped me hard on the back.

“It’s not like you’re an elementary school kid transferring schools. Just because you’re moving, you’re not going to stop seeing me, are you?”

“Of course I’ll see you. I definitely will.”

“Then it’s fine. Besides, I’m moving my stuff out by the end of today, too.”

“You are?”

“I told you last time. Don’t you remember?”

“Oh, right. You did.”

I had felt bad about leaving Jinho hyung alone in the goshiwon after all the years we had spent living together. Now I finally felt a little more at ease.

“Where are you moving?”

“Well, I ended up crashing at someone I know’s place. Where did you say the house you bought was?”

“Goyang. It’s only thirty minutes from here, so it’s not that far.”

“Goyang?”

Jinho hyung’s eyes widened.

“I’m in that area too, you punk!”

“Huh? Really?”

I was secretly pleased by the unexpected news. By now, his was a face I felt lonely not seeing for even a single day. If we lived close by, we could keep meeting often.

“Hyung, then where exactly is your address—”

Just as I was about to ask, the smartphone in my pocket rang. When I answered, a gravelly voice came from the other end.

—Hello, is this Mr. Jin Taekyung? I’m in front of the goshiwon right now.

“Ah, yes. Driver.”

It was the private moving-truck driver I had called in advance. I glanced out the window and saw a blue light truck waiting in front of the goshiwon.

—Do you have a lot of luggage? If anything’s heavy, I can help you carry it.

“No, it’s fine. I’ll carry it myself.”

I only had two things to move.

A cardboard box filled with small belongings, and…

*The capsule.*

Now that the Logout function had been activated, I no longer needed to use the capsule to travel between the Murim and modern worlds.

It had become nothing more than a bulky nuisance, but it held a more special meaning for me than anything else. That was the entire reason I had called a moving truck despite having so little luggage.

*What would have happened if I hadn’t had this capsule?*

I slowly ran my hand over its surface. The coldness of the metal and its rough texture traveled through my fingers.

This one old capsule had completely changed my life.

*Oh, right. There was also someone who played a major role in that.*

“Jinho hyung.”

“Yeah?”

I couldn’t help letting out a quiet laugh at his puzzled expression.

If Jinho hyung hadn’t gotten dead drunk that day, I never would have had a reason to enter the capsule.

“Never mind. It’s nothing.”

“You’re no fun. Anyway, shouldn’t you get going? There’s a truck waiting outside.”

“Yeah. Since you’re here, carry that box down for me. I have to carry the capsule, so I’m short on hands.”

“Uh, what?”

“What’s with that reaction? Can’t you carry one box for your little brother who’s moving away?”

“That’s not it… Ah, now that I think about it, I need to pack my own stuff too. Even if it’s a hassle, just make one trip back and forth. Well, good luck!”

“……”

Look at him slither away like a loach.

I watched Jinho hyung’s back as it slowly disappeared into the distance, then eventually picked up the box myself.

The moving driver, tired of waiting, honked the truck’s horn. The sound struck my ears.

Honk, honk!

“Yes, I’m coming down!”



* * *



“Are you a Hunter?”

The moving driver, who had been sneaking glances at me, finally spoke. The light truck, carrying the box and capsule, was heading toward my new home according to the navigation.

“How did you know?”

“You can tell at a glance. I used to be a Hunter, too. F-rank.”

“Oh, really?”

“I’m probably your Senior by training-center class. Ah, I’m not trying to pull rank. It would be ridiculous for a guy who quit after exactly one month and handed back his license to act like some old-timer.”

The driver continued, sounding as though he were simply airing a long-held grievance.

“Being a Hunter at the training center was manageable. Even though I was only F-rank, I took pride in becoming a Hunter. But the moment I joined a Guild after graduating, an accident happened.”

An accident at a Gate was synonymous with death.

Even if someone lost an arm or a leg, they could recover as long as they had enough money. Hunters didn’t call something that minor an accident.

“He was one of my training-center classmates, and he joined the Guild at the same time as me… Before I knew what was happening, he was dragged away and died just like that. I should have chased after him and saved him, no matter what it took, but I just couldn’t make myself move. After his funeral, I applied for retirement. Someone like me shouldn’t be going on raids.”

He tried to sound calm, but he couldn’t hide the tremor in his voice.

“I said something awfully ominous in front of a Hunter customer. It’s not exactly a pleasant story. Sorry about that.”

“Don’t worry about it.”

I understood how he felt.

I had experienced something similar. If I hadn’t felt responsible for my family, and if Jinho hyung hadn’t been there to comfort me, I might have retired two years ago.

*Then my life would have turned out completely differently.*

Being a Hunter was a brutal profession. The media praised them as humanity’s guardians and shields, but they lived with death always at their side.

—Turn right in fifty meters.

The driver flinched at the navigation’s voice, then muttered,

“Oh, come to think of it, this is a safe zone.”

“That’s right. Just keep going.”

“Ah, yes.”

The light truck arrived at its destination soon afterward.

It was a two-story detached house with a blue roof. A low stone wall surrounded a yard covered in grass. The house felt different from when I had first seen it a few days ago.

*It must be because it’s ours now.*

Our house.

The more I repeated those words in my head, the better they sounded. Of course, the fact that the house itself was beautiful probably helped.

“Wow… It’s a nice house.”

The driver climbed out of the cab and clicked his tongue in admiration. Praise sounded sweeter coming from someone else. No matter how hard I tried to suppress it, the corners of my mouth kept rising.

“You must be a successful Hunter. My dream was to live in a house like this.”

“Mine too.”

“Your wish came true. You must be happy.”

*Of course I was ecstatic.*

The driver continued exclaiming over the place, touching the stone wall and looking over the lawn, before asking,

“Would it be all right if I took a quick look inside? I can help move the capsule while I’m at it.”

“Sure. Go ahead.”

The moving driver became the new house’s first guest by accident as he climbed into the truck’s cargo bed.

He was going to move the capsule.

“That thing must weigh quite a bit.”

“It’s fine. I’ve moved plenty of them, so I know. Game capsules are all roughly the same weight.”

“No, it’s seriously heavy.”

I knew because I had lifted it myself earlier. It had been moderately heavy even for me, with my Strength stat in the triple digits. For the driver, it would be a different story entirely.

“Boss, I’ll move it myself.”

The driver hugged the capsule and grinned.

“Come on. You’re underestimating me. I may be an ex-Hunter, but something like this shouldn’t—nnngh!”

“Oh, wow.”

As expected of a former Hunter, he did manage to lift it in one go.

The only thing that had changed was that the smile had disappeared from his face.

“Go ahead and open the doors. Quickly!”

His voice suddenly urgent, I hurried over and threw open the front gate and the house’s entrance door. I had no idea why this had me feeling tense, too.

“I can carry it—”

“Move!”

“Ah, yes.”

He charged into the living room with the urgency of an alarm and shouted like he was screaming for his life.

“Which room?!”

“I was going to put the capsule upstairs…”

“What?!”

“…but just leave it in the nearest room.”

Fortunately, the door to one of the rooms was already open. With a heavy thud, the driver set down the capsule and began panting.

“Why… why is this… huff… so heavy?”

“……”

Hadn’t I told him it was heavy?



* * *



As soon as the moving driver left, I dropped onto the living room sofa.

It was one of the pieces of furniture the previous owner had transferred to me on the condition that I pay the remaining balance all at once.

*I’ll have to live alone for a few months.*

I had told my family that I was going back to Bucheon.

Until Hayeon finished her college entrance exam, I planned to eat and sleep here and commute to work.

*I need to remodel the house and buy a car, too. Ah, the Guild said they’d provide the car anyway, so I need to get my license first.*

There was a mountain of other things to do. But instead of feeling tired, I felt energized. These were all things I hadn’t been able to do before, no matter how much I wanted to.

It had only been a few months since I had done nothing but suffer while going back and forth between Gates and the goshiwon, yet so much had changed.

*You’ve come a long way, Jin Taekyung.*

One person suddenly came to mind.

A man who had always smiled like a boy despite his age. A man who had done his best for his wife and children and approached them like a friend.

*Dad, I bought a house. The place we used to live in was already gone. But I did well enough, right?*

I wanted to brag about it like a child, but the person who would have praised me had passed away long ago. All I could do was repeat, in my heart, words that could no longer reach him.

How much time passed like that?

When I came to my senses, it was already eight in the evening. The summer sun was slowly sinking.

*So this is how my last day of vacation ends.*

An entire week of vacation. It had been hectic because of everything involving the Sangdong Guild, but it was still the best rest I had enjoyed since becoming a Hunter.

Now it was time to return to my daily life.

*Precisely twelve hours from now.*

I lay flat on the sofa where I had been sitting. I briefly considered entering the capsule, but soon dismissed the thought.

After eleven years, I finally had a home of my own again. Just this once, I wanted to wake up in our living room instead of inside the stuffy capsule.

*Login.*

The System responded to my call.

Ding.

> **System**
>
> Would you like to connect to Murim?
>
> Y / N

Of course, my answer was yes.



* * *



A long time after Jin Taekyung lost consciousness, something no one could have expected was taking place in the room beside the front door.

Hissssss.

The door of the metal object that looked like a gigantic egg—the capsule—slowly began to open.

The first thing to emerge was a pair of feet.

Red letters were printed across a pair of long athletic socks that reached up to the calves.

**Hope Goshiwon Early-Morning Soccer Club**

Next came sweatpants rolled up halfway to the knees, followed by a pair of pale, skinny hands. The cover of the book he clutched tightly, as though it were scripture, gleamed in the sunset pouring through the window.

**Complete Mastery of the Civil Service Exam**

And finally, his face emerged.

After enduring several long hours of agony, he looked as haggard as Crown Prince Sado[^1] yet as relieved as Park Hyeokgeose emerging from an egg.[^2]

A parched voice slipped between his bone-dry lips.

“Is this my new nest…?”

As Seong Jinho gazed around the spacious room, a satisfied smile spread across his lips.

[^1]: Crown Prince Sado was an eighteenth-century Joseon royal who died after being confined in a wooden rice chest.

[^2]: Park Hyeokgeose is the legendary founder of the ancient Korean kingdom of Silla, said to have been born from an egg.
```
