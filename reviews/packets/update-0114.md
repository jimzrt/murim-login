<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0114.txt",
      "sha256": "c819582d4a0913c91b727b01868412d59250b6d4e1fba77ebe23bd93c39759b7",
      "bytes": 13779
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5409980f7c799fccd3f548f0a87b011616be4eb13be320f6bd97e71b2f23c7a3",
      "bytes": 1493
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7a7fd63457e4e46e02c2c19268e9838d60e419c10f9a3cdda6b329b2de665c0b",
      "bytes": 16602
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "485f301fa23c8e2ef30a47f4137ab6e345772ef9d4285ce44d5d36e6f26e6a86",
      "bytes": 724
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9288be8063f7cfc821c707bc634870307a0fc5083ebb9b3c334461e7bb106f6f",
      "bytes": 24117
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "acf47b8f90a36090d6ac1926a30de5cc606765e08e09f8267dc03e61d9801b76",
      "bytes": 749
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "e9383ff7caa74f472154b1f13799f77af21e751637e0b537e4e0c857e94a9272",
      "bytes": 684
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "982cd5b874d0f554868ea591830825c9ff2b47527434c6fdea4fe680879fee38",
      "bytes": 15822
    }
  ],
  "estimated_tokens": 17797
}
-->

# Durable State Update — Chapter 114

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 114. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 114. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 114,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 114,
    "continuity_sources": [114],
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
    "Pung Yang personally ordered the Red Wind Band's assault on the Mount Heng Sword Sect after the envoy's death.",
    "The Mount Heng Sword Sect's fortress defenses have become active in battle; the gate has been breached, while the walls remain the sect's final bulwark.",
    "Lee Seowol has directly commanded the defense, activated a concealed fire attack, and resolved to remain and lead the sect despite her fear of the battlefield.",
    "Cheol Mubaek is holding the breached gate alone, preventing the Red Wind Band from advancing through it.",
    "The Red Wind Band has suffered at least one hundred casualties but retains more than one hundred fifty and fewer than two hundred mounted bandits.",
    "Pung Yang has decided to confront the defenders personally and carries a hard wooden case containing an unidentified anti-tiger weapon or object."
  ],
  "continuity_sources": [
    113
  ],
  "open_questions": [
    "What is inside the hard wooden case Pung Yang carries?",
    "Whether Pung Yang can defeat Cheol Mubaek and break through the gate remains unresolved.",
    "Whether the Mount Heng Sword Sect will survive the continuing assault remains unresolved."
  ],
  "safe_through": 113,
  "temporary_decisions": [
    "Render 일류 초입 as early First Rate.",
    "Retain shichen and explain three shichen as six hours in context.",
    "Render 화시 as fire arrow, 쇠뇌 as crossbow, and 충차 as battering ram."
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
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |

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
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 영약     | **elixir**                                       |                                                       |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 사형     | **Senior Brother**                           |
| 선배     | **Senior**                                   |
| 체력               | **Stamina**                    |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 113
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 112
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 113
- **Aliases:** None
- **Role:** Current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 113
- **Aliases:** Red Wind Band Leader
- **Role:** Leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

## Korean source

```text
＃114화



항산호 철무백은 철탑처럼 서 있었다.

뻥 뚫린 입구는 마차 두 대가 지나가고도 남을 만큼 넓었지만 오십여 명의 적풍단은 아무도 발을 내딛지 못했다.

앞서 나섰던 동료들이 어떻게 죽었는지 똑똑히 봤기 때문이다.

머리가 터져 죽고, 복부를 뚫려 죽고, 사지가 꺾여서 죽었다. 철무백의 일권(一拳)이 언제, 어떻게 움직였는지 제대로 본 사람은 없었다.

그렇게 죽은 이가 스물이 넘었다.

“괴물…….”

공포에 잠긴 그들을 구원한 것은 뒤에서 들려온 누군가의 중후한 목소리였다.

“너희들은 이만 가 보거라. 여긴 내가 맡겠다.”

목소리의 주인, 적풍단주 풍양의 등장에 마적들이 썰물처럼 물러났다. 두 절정 고수는 그제야 서로를 마주했다.

“다시 뵙소, 철 선배.”

“도적놈을 후배로 둔 기억은 없는데.”

“까칠한 건 여전하시구려. 옷깃만 스쳐도 인연이라는데, 선배와 나는 손까지 섞은 사이 아니오?”

“그랬지. 네놈은 뒤도 안 돌아보고 도망쳤고.”

“전략적 후퇴라고 해 둡시다. 나도 거기서 철 선배가 등장하실 줄은 몰랐으니까.”

“내상은 다 나았나?”

“속이 뜨거워서 며칠 혼났지요. 그래도 죽을 정도는 아니라 염치 불고하고 다시 찾아온 것 아니겠소?”

“오늘은 뜨거운 정도로 끝나지 않을 게다.”

“저런, 대화로 푸는 건 어떻겠소? 연세도 꽤 지긋하신 분이 성격이 이리 불같아서야…….”

풍양의 능청스러운 말에 철무백이 이를 갈았다.

“대화? 네가 배신하지 않았더라면 천백, 그 친구는 살 수도 있었다.”

“승산 없는 싸움에 끼어들 정도로 멍청한 놈은 아니라서 말이오.”

“그것으로 부족해서 소광이마저 죽였느냐?”

“주제도 모르고 덤비는 어린놈을 살려 줄 만큼 유한 성격도 아니고.”

풍양이 부드럽게 웃으며 말을 이었다.

“그 어린놈이 내 처남이 될 줄 알았다면 살려 뒀겠지만 말이오.”

“이노옴!”

철무백의 전신에서 용암 같은 기세가 끓어올랐다. 절정 고수의 강대한 열양지기에 지면을 덮은 눈이 녹아내리고 초목이 노랗게 물든다.

그 광경에 풍양이 탄성을 토해 냈다.

“역시 대단한 공력이오. 철 선배가 마음만 먹었다면 오늘 내가 상대하는 것은 항산권문(恒山拳門)이 되었겠군.”

“네놈의 사지를 뽑아 주마.”

“글쎄, 너무 자신하지 않는 게 좋을 거요.”

“지난번 같은 요행은 바라지 마라. 오늘은 방패막이로 사용할 놈들도 없으니.”

풍양이 빙긋 웃었다.

“내가 수하들을 물린 이유가 뭐겠소?”

“그건…….”

철무백은 멈칫했다. 안 그래도 아까부터 풍양의 여유로운 태도가 마음에 걸리던 찰나였다.

‘무슨 꿍꿍이지?’

지난번에는 불과 백여 합 만에 내상을 입고 물러났던 풍양이다. 수하들을 방패 삼아 도망쳤던 그가 모두를 물리고 제 발로 찾아왔다는 것은 그만큼 자신이 있단 소린데…….

“무슨 개수작이냐?”

“개수작이라니, 호랑이에게 닭 잡는 칼을 쓸 수 없어 직접 나섰을 뿐이오.”

“네깟 놈 혼자?”

“안될 것 있겠소?”

“그럴 리가. 나야 고마울 따름이지.”

의구심 어린 눈빛으로 풍양을 노려보던 철무백이 주먹을 말아 쥐었다.

“덕분에 일이 쉽게 끝나게 됐으니 말이다.”

후우웅.

말이 끝남과 동시에 뜨거운 열풍이 바로 앞으로 들이닥쳤다. 풍양은 숨을 삼키며 가슴을 노리고 날아드는 붉은 권기(拳氣)를 향해 곡도를 휘둘렀다.

쾅! 쾅쾅!

두 절정 고수의 격돌. 연달아 터지는 굉음과 함께 몰아친 바람이 눈 덮인 바닥을 휩쓸었다.

높이 솟구친 눈 더미 아래, 한 사람이 비틀거리며 물러났다.

“으음.”

풍양이 침음을 삼키며 찢어진 손아귀를 바라봤다. 볼썽사납게 병장기를 놓치는 것은 면했으나 힘의 차이는 확실했다.

“역시 강하구려.”

철무백이 풍양을 향해 걸음을 내디디며 대답했다.

“후회해도 늦었다.”

“이하 동문이오.”

“주둥이부터 찢어 놔야겠군.”

쐐애애액!

철무백은 호랑이 같은 몸놀림으로 달려들었다.

오래전 실전되었다고 알려진 수라멸권(修羅滅拳)의 강맹한 초식들이 풍양을 향해 쏟아졌다.

콰과광!



* * *



성벽에서는 치열한 혈투가 벌어지고 있었다. 자그마치 네 배에 달하는 병력의 차이가 있지만 항산검문의 무인들은 물러서지 않았다.

“물러서면 죽음뿐이다!”

“마적 놈들에게 고향을 뺏길 셈이냐!”

“놈들에게 죽은 사형제들의 원수를 갚자!”

서걱, 푹!

“크아악!”

“미, 밀지 마!”

적풍단의 마적들은 혼란에 빠졌다. 앞서 당한 화공의 영향과 또 다른 함정이 있을지 모른다는 두려움이 발목을 잡았다.

그들은 자신들과는 반대로 눈이 뒤집혀 달려드는 항산검문 무인들의 파죽지세에 속수무책으로 썰려 나갔다.

“도망치지 마라!”

“물러서는 놈들은 내 손에 뒈질 줄 알아!”

조장 격인 마적들이 목청껏 외쳤지만 혼란을 수습하는 건 역부족이었다. 오히려 그들 또한 어디서 날아왔는지 모를 화살에 목숨을 헌납해야 했다.

푸푹!

“크륵. 커어어…….”

“조, 조장!”

이소월은 가장 높은 망루에 서서 쉼 없이 활시위를 당겼다.

그녀의 곁에는 항산검문의 무인 중 가장 활을 잘 다루는 다섯 명의 궁수가 함께했다.

퉁! 푹!

시위가 당겨질 때마다 한 명의 마적들이 쓰러진다. 조장, 혹은 그 이상으로 보이는 자들이 최우선으로 노려야 할 표적이었다.

‘한 놈이라도 더, 더.’

그러나 전황은 생각 이상으로 어렵게 흘러가고 있었다.

처음부터 적은 병력으로 전투에 임했던 항산검문의 무인들은 빠른 속도로 지쳐 갔고, 이내 하나둘씩 눈먼 칼날에 목숨을 잃고 있었다.

반면 마적들은 점차 혼란에서 빠져나오는 중이었다.

“정신 차려! 항산검문 놈들은 몇 안 돼!”

“이놈들만 죽이면 우리의 승리다!”

더 이상 잃을 게 없는 항산검문의 무인들 역시 불리한 전황에도 아랑곳하지 않고 필사적으로 맞섰다.

“죽여라!”

서걱, 서걱, 서걱!

그러나 마적 하나를 베면 둘이, 둘을 베면 셋이 나타나 빈자리를 메웠다.

“헉, 허억!”

정신없이 검을 휘두르는 항산검문의 무인을, 사방에서 튀어나온 대여섯 개의 병장기가 난도질한다.

서걱! 푸푸푹!

목, 가슴, 복부……. 전신이 베이고 꿰뚫린 채 비명 한 번 못 지르고 죽는 무인들이 곳곳에서 속출했다.

기세가 오른 적풍단의 마적들은 쉬지 않고 몰아쳤다. 어느새 성벽의 절반이 적들로 가득 찼다.

“하아, 하아.”

퉁, 퉁, 퉁!

이소월은 젖 먹던 힘까지 끌어모아 활시위를 당겼다. 섬섬옥수 같던 손가락과 악문 잇새에서는 피가 흘렀고 바짝 말라붙은 입 안에서는 단내가 풀풀 풍겼다.

“저기다!”

쉴 새 없이 화살을 쏘아 댄 탓에 결국 얼마 지나지 않아 위치가 발각됐다. 이십여 명의 마적들이 방패를 세우고 망루로 돌격해 오자 다급한 외침이 터져 나왔다.

“문주!”

“피하셔야 합니다! 놈들이 오고 있습니다!”

공성전이 시작되고 이제 세 시진. 취미 삼아 활을 수련했을 뿐, 무인이 아닌 이소월의 체력은 한계에 다다른 지 오래였다.

그러나 그녀는 멈추지 않았다. 덜덜 떨리는 가느다란 팔뚝에 억지로 힘을 주고 다음 표적을 찾았다.

‘피해? 어디로?’

평생을 이곳에서 살았다. 항산검문은 이소월에게 있어 고향이자 생애 마지막 순간까지 지켜야 할 무언가였다.

그것은 지금까지도 최후의 항전을 이어 가는 무인들에게도 마찬가지였다.

“놈들을 막아라!”

“결코 문주께 보내서는 안 된다!”

필사적인 외침이 무색하게도 이미 성벽은 점령당한 뒤였다.

살아남은 항산검문의 무인들은 망루로 퇴각했다. 그러나 일백은 족히 넘어 보이는 마적들이 사방에서 조여 오고 있었다.

적들이 들고 있는 횃불 사이로 살기와 욕망으로 번들거리는 눈동자들이 비친다.

“이 망할 년놈들이 감히…….”

“한 놈도 빠짐없이 갈기갈기 찢어 개밥으로 던져 주마.”

둥글게 망루를 포위한 마적들의 살기가 피부를 찔렀다.

모두 절망에 빠진 그때, 이소월이 돌연 하늘을 향해 활시위를 당겼다.

후우웅.

불의 꼬리를 늘어트리며 떨어지는 한 발의 화시(火矢)의 목적지는 어둠에 잠긴 성문.

그것은 한 사람을 찾기 위한 불빛이었다.

‘철 숙부.’

항산호 철무백. 그가 항산검문의 마지막 희망이다.

불화살이 밝힌 불빛 아래로 한 사람이 걸어 나온 것은 그때였다.

저벅. 저벅.

“이제 와서 말하긴 뭣하지만…….”

단 한 번 들었을 뿐이지만 꿈에서도 잊지 못하는 목소리.

차마 쳐다보지 못하고 눈을 감는 이소월에게, 풍양이 활짝 웃어 보였다.

“나와 혼인해 줘야겠소.”



* * *



사냥꾼 철무백이 항산의 호랑이가 될 수 있었던 이유는 기연(奇緣)을 만났기 때문이다.

광활한 항산 산맥의 어느 산자락에서 늑대를 추적하던 그는 절벽 사이 숨겨져 있던 비동(秘洞)으로 추락했고, 그곳에서 은거 고수가 남긴 비급과 영약을 발견했다.



‘나는 돌아간다. 반드시 살아 돌아간다!’



철무백은 살기 위해 무공을 익혔다. 비동에 있던 벽곡단이 떨어지자 절벽 사이에 난 풀을 뜯어 먹거나 박쥐를 잡아먹으며 수련했다.

자그마치 삼 년 만에 맨손으로 절벽을 기어올라 마을로 돌아간 그를 기다리고 있던 것은 폐허가 된 집, 그리고 아내와 자식의 죽음이었다.



‘소식이 끊긴 지 두어 달쯤 됐나? 평소 자네 내자를 눈독 들이고 있었던 황가 놈이…….’



정신을 차렸을 때는 이미 마을의 대지주와 그의 하인들을 모두 때려죽인 후였다.

원수를 갚은 철무백은 다시 비동으로 돌아가 무공을 수련했다. 그건 스스로에 대한 채찍질이었고 가족에 대한 속죄였다.

그렇게 시간이 얼마나 흘렀을까, 어느새 철무백은 항산의 호랑이라 불리고 있었다.

하지만…….

“후욱, 호랑이가, 울겠군.”

철무백은 거칠게 숨을 몰아쉬었다. 형형하던 눈빛은 먹구름이 낀 것처럼 흐렸고 수염은 피로 흠뻑 젖었다.

‘어서 가야 하는데, 놈을 막아야 하는데…….’

그러나 그에게 남아 있는 것은 의지뿐, 사지가 부러진 몸은 이미 통제를 벗어났다. 항산호(恒山虎)라는 별호가 아깝지 않은 무공을 펼쳤건만 풍양을 꺾을 수는 없었다.

‘그놈이 도대체 어떻게.’

결과는 분명해 보였다. 풍양은 이제 간신히 도기(刀氣)를 만들어 내는 절정 초입의 경지였고 철무백은 완숙한 경지에 오른 절정 고수였다.

바람 앞의 촛불처럼 위태롭던 풍양이 돌변한 것은 품에서 정체불명의 목곽을 꺼낸 후였다.

‘붉은 단환. 맞아, 분명히 그거였어.’

암기인가 싶어 물러난 것이 실수였다. 단환을 꿀꺽 삼킨 풍양은 더 이상 철무백이 알던 일개 마적단의 우두머리가 아니었다.

‘어찌 인간이 그토록 강해질 수 있단 말인가.’

풍양의 움직임을 떠올린 철무백의 눈가가 파르르 떨렸다.

열 번, 백 번을 다시 겨룬다 해도 이길 수 없을 것 같은 아득한 격차. 한순간에 전세를 역전시킨 풍양은 그의 사지를 부러뜨리고 막대한 내상을 입힌 다음 떠났다.



‘당장은 살려 주지. 이번 혼인의 예물로 당신의 무공 구결을 받고 싶어졌거든.’



떠나기 전, 풍양이 남긴 말을 떠올린 철무백의 눈가가 붉게 물들었다. 수라멸권은 일인전승, 비인부전의 무공이다.

풍양에게 넘기느니 자결을 택하겠지만 딸처럼, 손녀처럼 아끼는 이소월이 마음에 걸렸다.

‘도대체 이를 어찌해야 한단 말인가.’

철무백이 먹먹한 심정으로 하늘을 바라보던 그 순간이었다.

두두두!

멀리서 들려오던 말발굽 소리가 점점 가까워지더니, 철무백의 발치에서 우뚝 멈췄다. 휘영청 밝은 달 아래, 그를 내려다보는 네 쌍의 시선이 있었다.

“적풍단 애들은 정년도 없나. 웬 노인네까지 마적질을.”

“진 공자, 항산호 철무백 대협이에요.”

“헉, 죄송합니다. 야, 무진아. 얼른 사과드리지 않고 뭐 해.”

“실수는 조장이 했는데 왜 제가…….”

빡!

“할아버지, 아니 대협. 괜찮으세요?”

철무백은 대답 대신 청년의 가슴팍을 뚫어져라 바라봤다.

남색 무복에 새겨진 한 글자.

진(進).

“태원……진가?”

“어, 알아보시네?”

청년, 진태경이 씩 웃었다.
```

## Final English reading copy

```markdown
# Chapter 114

The Tiger of Mount Heng, Cheol Mubaek, stood like an iron tower.

The entrance gaped wide enough for two carriages to pass through side by side, yet not one of the fifty-odd mounted bandits of the Red Wind Band dared set foot inside.

They had seen clearly how the men who went ahead of them had died.

Some had died with their heads blown apart. Others had been pierced through the abdomen or killed when their limbs were broken. No one had properly seen when or how Cheol Mubaek’s fist moved.

More than twenty had died that way.

“Monster…”

A deep voice from behind rescued the mounted bandits, who were paralyzed with fear.

“You’ve done enough. Go on now. I’ll handle this place.”

At the appearance of the voice’s owner, Pung Yang, the Red Wind Band Leader, the mounted bandits retreated like the tide going out. Only then did the two Peak masters face each other.

“Good to see you again, Senior Cheol.”

“I don’t recall ever taking a bandit as a junior.”

“You’re still as prickly as ever. They say even brushing sleeves with someone creates a connection, and you and I have crossed hands, haven’t we?”

“We did. Then you ran away without even looking back.”

“Let’s call it a strategic retreat. I didn’t expect Senior Cheol to show up there, either.”

“Are your internal injuries healed?”

“My insides were burning, so I had a rough few days. But it wasn’t enough to kill me, which is why I’ve come back despite my shame.”

“Today, it won’t end with mere heat.”

“Oh, dear. How about we settle this through conversation? For a man of your age to have such a fiery temper…”

At Pung Yang’s shameless remark, Cheol Mubaek ground his teeth.

“Conversation? If you hadn’t betrayed us, Lee Cheonbaek, my friend, might have lived.”

“I’m not stupid enough to join a fight with no chance of winning.”

“As if that weren’t enough, you killed Lee Seogwang too?”

“I’m not softhearted enough to spare a brat who came at me without knowing his place.”

Pung Yang smiled gently and continued.

“If I’d known that brat would become my brother-in-law, I might have spared him.”

“You bastard!”

A lava-like aura boiled up from every inch of Cheol Mubaek’s body. Under the formidable Scorching Yang Qi of a Peak master, the snow blanketing the ground melted away, and the vegetation turned yellow.

Pung Yang let out an exclamation at the sight.

“Your internal energy really is remarkable. If Senior Cheol had only set his mind to it, the opponent I faced today would have been the Mount Heng Fist Sect.”

“I’ll tear your limbs from your body.”

“Still, you shouldn’t be too confident.”

“Don’t expect the same stroke of luck as last time. Today, you won’t have anyone to use as a shield.”

Pung Yang smiled faintly.

“Why do you think I sent my men away?”

“That…”

Cheol Mubaek hesitated. Pung Yang’s relaxed attitude had been bothering him for some time.

*What is he plotting?*

Last time, Pung Yang had withdrawn after suffering internal injuries in barely a hundred exchanges. The fact that the man who had used his subordinates as shields to escape had sent everyone away and come here of his own accord meant that he was confident enough to do so…

“What kind of dirty trick are you planning?”

“A dirty trick? I simply couldn’t use a chicken-killing knife on a tiger, so I stepped in myself.”

“You? Alone?”

“Is there any reason I can’t?”

“There’s no way. I’m grateful, if anything.”

Cheol Mubaek glared at Pung Yang suspiciously and clenched his fists.

“Thanks to you, this will be over easily.”

Whoooosh!

The instant he finished speaking, a scorching gale rushed straight toward Pung Yang. Pung Yang swallowed a breath and swung his curved saber at the red fist energy flying toward his chest.

Boom! Boom-boom!

The two Peak masters collided. Roaring explosions rang out one after another, and the resulting wind swept across the snow-covered ground.

Beneath a mound of snow that had leaped high into the air, one man staggered backward.

“Ugh.”

Pung Yang swallowed a groan and looked at his torn palm. He had avoided the disgrace of dropping his weapon, but the difference in strength was undeniable.

“You’re still as strong as ever.”

Cheol Mubaek stepped toward him and answered.

“You’ll regret this, but it’s already too late.”

“I feel the same way.”

“I’ll have to tear that mouth of yours apart first.”

Fwoooooosh!

Cheol Mubaek lunged forward with the movements of a tiger.

The fierce forms of the long-lost Shura Annihilating Fist poured down upon Pung Yang.

Kwa-gwa-gwang!

* * *

A fierce bloody battle was raging along the fortress walls. Despite facing a four-to-one disadvantage in numbers, the martial artists of the Mount Heng Sword Sect refused to retreat.

“Retreat, and all that awaits us is death!”

“Are you going to let those mounted-bandit bastards take our home from us?”

“Let’s avenge the martial brothers they killed!”

Slice! Thrust!

“Aaargh!”

“D-don’t push me!”

The mounted bandits of the Red Wind Band had fallen into confusion. The effects of the earlier fire attack and the fear that another trap might be waiting held them back.

In stark contrast, the martial artists of the Mount Heng Sword Sect charged at them wild-eyed. The mounted bandits were helpless against their unstoppable momentum and were cut down one after another.

“Don’t run away!”

“Any bastard who retreats dies by my hand!”

The mounted bandits who served as squad leaders shouted at the top of their lungs, but they were unable to restore order. Instead, they too had to surrender their lives to arrows that seemed to fly out of nowhere.

Thwack!

“Ghk. Gaaah…”

“Squad Leader!”

Lee Seowol stood atop the highest watchtower, drawing her bowstring without pause.

Beside her were the five best archers among the martial artists of the Mount Heng Sword Sect.

Twung! Thud!

Every time a bowstring was drawn, a mounted bandit fell. Squad leaders, or those who appeared to rank even higher, were their highest-priority targets.

*One more. One more.*

But the battle was unfolding more harshly than expected.

The martial artists of the Mount Heng Sword Sect had entered the battle with fewer troops from the very beginning. They grew exhausted at an alarming rate, and before long, one or two at a time began losing their lives to stray blades.

The mounted bandits, meanwhile, were gradually recovering from their confusion.

“Get a grip! There aren’t many of these Mount Heng Sword Sect bastards!”

“If we kill these men, victory is ours!”

The martial artists of the Mount Heng Sword Sect had nothing left to lose. They fought desperately, disregarding their disadvantage.

“Kill them!”

Slice! Slice! Slice!

But every time one mounted bandit was cut down, two more appeared to fill the gap. When two were cut down, three took their place.

“Gasp, gasp!”

A martial artist of the Mount Heng Sword Sect swung his sword frantically, only to be hacked apart by five or six weapons that sprang at him from every direction.

Slice! Thud-thud-thud!

His neck, chest, abdomen… Martial artists were cut and pierced all over, dying without even having time to scream. Their bodies fell in growing numbers.

The mounted bandits of the Red Wind Band, their momentum rising, continued pressing the attack without pause. Before anyone realized it, half the fortress wall was packed with enemies.

“Haa, haa.”

Twung! Twung! Twung!

Lee Seowol summoned every last bit of strength she had and drew her bowstring. Blood ran from her once-delicate fingers and between her clenched teeth, while the dry inside of her mouth reeked of a sickly sweetness.

“There!”

After firing arrows without rest, her position was discovered before long. When about twenty mounted bandits raised their shields and charged toward the watchtower, desperate shouts rang out.

“Sect Leader!”

“You have to get away! They’re coming!”

Three shichen—six hours—had passed since the siege began. Lee Seowol had only practiced archery as a hobby. She was not a martial artist, and her Stamina had reached its limit long ago.

But she did not stop. She forced strength into her thin, trembling arms and searched for her next target.

*Escape? Where would I go?*

She had lived here her entire life. To Lee Seowol, the Mount Heng Sword Sect was both her hometown and something she had to protect until the final moment of her life.

The same was true for the martial artists who continued their last stand.

“Stop them!”

“Never let them reach the Sect Leader!”

Their desperate cries were futile. The fortress walls had already been overrun.

The surviving martial artists of the Mount Heng Sword Sect retreated to the watchtower. But more than a hundred mounted bandits were closing in from every direction.

Eyes gleaming with killing intent and desire shone between the torches held by the advancing enemies.

“You damned bastards dare…”

“I’ll tear every last one of you limb from limb and throw you to the dogs!”

The killing intent of the mounted bandits surrounding the watchtower in a circle stabbed at their skin.

Just as everyone was falling into despair, Lee Seowol suddenly drew her bowstring toward the sky.

Whoooosh.

Trailing a tail of fire, a single fire arrow descended toward the gate, which was shrouded in darkness.

It was a light meant to find one person.

*Uncle Cheol.*

The Tiger of Mount Heng, Cheol Mubaek. He was the Mount Heng Sword Sect’s final hope.

That was when a man walked out beneath the light revealed by the fire arrow.

Clomp. Clomp.

“I suppose it’s a little late to say this now…”

Lee Seowol had heard that voice only once, but she could never forget it, not even in her dreams.

Unable to bring herself to look at him, she closed her eyes.

Pung Yang smiled broadly at her.

“You’ll have to marry me.”

* * *

The hunter Cheol Mubaek became the Tiger of Mount Heng because of a fortuitous encounter.

While tracking wolves along a mountainside in the vast Mount Heng range, he fell between cliffs into a hidden cave. There, he discovered a martial arts manual and an elixir left behind by a reclusive master.

*I’m going back. I’m going back alive, no matter what!*

Cheol Mubaek learned martial arts to survive. When the fasting pills in the hidden cave ran out, he tore up grass growing between the cliffs or caught bats to eat as he trained.

After no less than three years, he climbed the cliff with his bare hands and returned to the village.

What awaited him was his home in ruins—and the deaths of his wife and child.

*Had it been a couple of months since we lost contact? That bastard Hwang, who’d always had his eye on your wife…*

By the time he came to his senses, he had already beaten the village’s leading landowner and all his servants to death.

After avenging his family, Cheol Mubaek returned to the hidden cave and resumed his martial arts training. It was a whip he used against himself, and atonement for his family.

How much time passed like that?

Before he knew it, Cheol Mubaek was being called the Tiger of Mount Heng.

But…

“Hoo. Even a tiger would cry.”

Cheol Mubaek panted harshly. His once-brilliant eyes were clouded like a sky covered in dark clouds, and his beard was drenched in blood.

*I have to hurry. I have to stop that bastard…*

But all he had left was his will. His body, with its limbs broken, had already slipped beyond his control. He had displayed martial arts worthy of the title Tiger of Mount Heng, yet he still could not defeat Pung Yang.

*How in the world did he…?*

The result seemed obvious. Pung Yang had only just entered the Peak realm, barely capable of creating blade qi, while Cheol Mubaek was a Peak master who had reached a mature realm stage.

Pung Yang had been as precarious as a candle in the wind. Then he had suddenly changed after pulling an unidentified hard wooden case from inside his robes.

*The red pill. Yes, that was definitely it.*

Cheol Mubaek had made a mistake by retreating because he thought it might be a hidden weapon. After Pung Yang gulped down the pill, he was no longer the leader of the ordinary mounted-bandit group Cheol Mubaek had known.

*How can a human being become that strong?*

Cheol Mubaek’s eyes trembled as he recalled Pung Yang’s movements.

The gap between them was so vast that it seemed impossible to win, even if they fought ten or a hundred more times. Pung Yang had overturned the battle in an instant, broken all four of Cheol Mubaek’s limbs, inflicted massive internal injuries, and then left.

*I’ll let you live for now. I’ve decided I want your martial arts formula as a wedding gift.*

Cheol Mubaek’s eyes reddened as he recalled Pung Yang’s parting words.

The Shura Annihilating Fist was a martial art passed down to a single successor and never taught to outsiders.

He would choose suicide rather than hand it over to Pung Yang, but Lee Seowol—whom he cherished like a daughter or granddaughter—troubled him.

*What on earth am I supposed to do?*

It was at that moment, as Cheol Mubaek stared at the sky with a heavy heart, that it happened.

Thud-thud-thud-thud!

The sound of approaching hooves grew louder and louder before coming to a sudden stop at his feet.

Beneath the brilliantly shining moon, four pairs of eyes looked down at him.

“Doesn’t the Red Wind Band have a retirement age? Why is an old geezer still out here playing bandit…?”

“Young Master Jin, that’s Great Hero Cheol Mubaek, the Tiger of Mount Heng.”

“Gah! I’m sorry. Hey, Mujin. Hurry up and apologize. What are you waiting for?”

“The squad leader is the one who made the mistake, so why should I…?”

Smack!

“Grandpa—no, Sir. Are you all right?”

Instead of answering, Cheol Mubaek stared intently at the young man’s chest.

One character was embroidered on his navy martial robe.

進.

“Taiyuan… the Jin Family?”

“Oh, you recognize it?”

The young man, Jin Taekyung, grinned.
```
