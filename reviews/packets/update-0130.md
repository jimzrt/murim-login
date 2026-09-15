<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0130.txt",
      "sha256": "6eef33d04bf805f367319e5906034f6a7b7c1c3de949f3b487b2e41b6c179430",
      "bytes": 14297
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "19a97878e01d3af7bedc3db77d8910352b9153e28c8cf76fa884e6e9dbccb297",
      "bytes": 6672
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c858a230943cc5600b22be63ba520a99d2416c6177e4ed890ff06d702b5ac5e3",
      "bytes": 23505
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8c5ce19286fca31f66d1739b0eb2d4090d82cde0f91f9802440de8bd5f5287d5",
      "bytes": 20060
    }
  ],
  "estimated_tokens": 20986
}
-->

# Durable State Update — Chapter 130

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 130. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 130. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 130,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 130,
    "continuity_sources": [130],
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
    "Pung Yang is dead; Jin Taekyung killed him after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest.",
    "Taekyung fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.",
    "Jin Mukyung survived his fight with Pung Yang and returned to the Jin Family of Taiyuan, but remains incompletely recovered.",
    "Cheol Mubaek remains severely injured and needs extended recuperation; Lee Seowol remains the seventeen-year-old Sect Leader of the Mount Heng Sword Sect and vows to preserve it.",
    "The Lower District Sect sent a relief force with physicians, cooks, and laborers after the battle.",
    "Wolhwa's real name is Eun Sowol, and she is the Lower District Sect's Shanxi Branch Leader with authority over more than thirty Shanxi branches.",
    "Lee Seowol accepted Jin Wikyung's invitation to the Jin Family of Taiyuan's New Year gathering and offered the Mount Heng Sword Sect's territorial rights to the Jin Family as an apology.",
    "Lee Seowol proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist; Taekyung decided to reject the proposal because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty with its available medicine; the sect is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued Mount Heng.",
    "Cheol Mubaek and Lee Cheonbaek first met more than thirty years ago, fought, and became close friends; Cheol is the ninth-generation successor of the Shura Annihilating Fist.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm; the Fire King is a Supreme Peak master and the Fire Gate Clan has a single successor, but his current status is unknown.",
    "The Mount Heng Sword Sect formally apologized for Lee Cheonbaek's crimes, but Taekyung refused the apology and directed responsibility toward the Jin Family of Taiyuan.",
    "The Temporary Strength Pill is stored in Taekyung's Inventory and has been revealed to Jin Wikyung, Jin Mukyung, and Wipeng; its System description identifies Dark Heaven as its manufacturer and records its unknown Grade, Peak restriction, temporary power increase, +100 combat stats, fifteen years of internal energy, and Body-Protecting Qi effect.",
    "Jin Wikyung and Wipeng traveled to Sakju with fifty elite guards after receiving an emergency report about Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, and the Jin brothers.",
    "The Jin Family of Taiyuan displayed a huge Sakju banner celebrating the safe return of Mukyung, Taekyung, and Hyuk Mujin.",
    "Taekyung, Mukyung, Wikyung, and Wipeng drank through the night for three days; Wipeng is called the God of Drinking and Taekyung is rumored to be the Night King.",
    "Taekyung's Sleeping Dragon of Shanxi Title effect strengthened to all stats +15 and Fame +200; his current Status Window shows Level 61, Fame 2,100 (+250), and 60 remaining points.",
    "Hyuk Mujin and Taekyung publicly exaggerated the battle's death toll and achievements, and the county magistrate and assembled crowd reacted with awe.",
    "Hyuk Mujin accepted the City Lord's Invitation Quest for Taekyung, which requires attendance at the City Lord's luncheon with young prodigies tomorrow; its reward depends on the City Lord's reaction and rejection may make him sulk.",
    "The City Lord of Shanxi Province is a ten-year-old Prince and the Emperor's youngest brother, appointed at age five; Jin Mukyung met him after being summoned three years earlier and considered the encounter a nightmare."
  ],
  "continuity_sources": [
    129,
    128
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What are the Temporary Strength Pill's exact price and long-term aftereffect, and is it related to the Demonic Cult's Blood-Exploding Pill?",
    "What is Dark Heaven, and why do Jin Wikyung and Wipeng refuse to discuss it?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "Was Jopil truly the nineteenth-generation successor of the Flame Divine Palm, and how did he acquire it?",
    "What will happen at the City Lord's luncheon and how will the City Lord react to Taekyung?"
  ],
  "safe_through": 129,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 폭혈단 as Blood-Exploding Pill.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, and 시진 as shichen.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, 천하십대권법 as the ten greatest fist techniques in the world, 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, 아이템창 as Item Window, 전서응 as messenger eagle, 고원 as Gaoyuan, 구주 as Nine Provinces, 사술 as dark arts, 마기 as demonic qi, 선천지기 as innate qi, 소음인 as Soeumin, 태양인 as Taeyangin, 암천 as Dark Heaven, 주신 as God of Drinking, 야왕 as Night King, 화주 as fire liquor, 화북 as North China, 현령 as county magistrate, 성주 as City Lord, 장 노인 as Old Man Jang, 적토마 as Red Hare, 여포 as Lü Bu, 성주의 초청 as The City Lord's Invitation, 친왕 as Prince, 주씨 as Zhu, 천자 as Son of Heaven, 황상 and 황제 as Emperor, 태자 as Crown Prince, 구파일방 as Nine Sects and One Gang, and 오대세가 as Five Great Families."
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
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |

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
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |

## Exact glossary matches

| 무림     | **Murim**          |
| 청풍     | **Cheongpung**     |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 마적     | **mounted bandits**                              |                                                       |
| 표국     | **Escort Bureau**                            |
| 표사     | **escort**                                   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |

## Listed compact profiles

(No chapter-safe profiles matched.)

## Korean source

```text
＃130화



변방의 겨울은 혹독하다. 옷깃을 파고드는 칼바람에 중년 사내가 몸을 부르르 떨었다.

“어흐으, 더럽게 춥네.”

사내, 석칠은 산서성 남부에 있는 성운표국(盛運鏢局)의 쟁자수다.

하루 반나절이 넘게 백 근(斤)이 넘어가는 짐수레를 끌어 온몸이 땀으로 흠뻑 젖었고, 지금처럼 잠시 휴식을 취할 때는 엄청난 한기와 싸워야 했다.

“형님, 짐수레 얼른 놓고 빨리 와서 불이나 좀 쬐시오. 그러다가 얼어 죽겠네.”

어느새 모닥불 앞에 쭈그려 앉은 동료 쟁자수가 말했다. 석칠은 퉁명스럽게 대답하며 걸음을 옮겼다.

“이놈아, 내가 먹여 살려야 할 입이 다섯이다. 죽으려면 한참 멀었어.”

“그렇지. 여우 같은 마누라와 토끼 같은 자식들 생각하면 못 죽지.”

“여우는 무슨. 곰이야, 곰.”

“방금 그거 유언이오? 형수님이 들으면 모가지를 꺾어 버릴 텐데.”

“없는 데서는 나라님 욕도 하는 법이야. 몰라?”

석칠은 모닥불 앞으로 바짝 다가갔다.

말똥을 장작으로 쓰다 보니 고약한 냄새가 사방으로 풍겼지만 이십 년 가까이 쟁자수 일을 해 온 그에게는 밥 짓는 냄새만큼이나 익숙했다.

“어따, 이제야 좀 살겠다.”

“그런데 형님, 너무 야박한 거 아니오?”

“응? 이건 또 무슨 헛소리야?”

동료 쟁자수가 실실 웃으며 턱짓했다.

“신참도 데려오셔야지. 혼자만 살겠다고 냅다 오는 법이 어디 있소?”

꽁꽁 언 손을 녹이던 석칠이 고개를 돌렸다. 그의 시선 끝에 멀뚱멀뚱한 얼굴로 눈 덮인 바위 위에 앉아 있는 한 청년이 보였다.

‘저놈 저거, 또 저러고 있네.’

청년은 하남(下南)에서 새로 구한 쟁자수다. 이번 표행의 책임자인 송 표두에게 듣기로는 그럭저럭 밥값은 할 것 같아 받아 줬다고 한다.

‘뭐, 사람이야 늘 부족하니까.’

문제는 젊은 놈이 대체 무슨 생각을 하는지, 지금처럼 넋 놓고 있을 때가 많다는 거다.

쯧쯧 혀를 차는 석칠에게 동료 쟁자수가 물었다.

“왜요, 좀 이상한 놈입니까?”

“일은 잘해. 보기보다 힘이 장사더라고.”

“그럼 됐지, 뭘.”

“되긴 뭐가 돼. 젊은 놈이 허구한 날 저러고 있으니 답답해서 그렇지. 나 때는 말이야…….”

“풍운의 꿈을 품고 하루하루 열심히 살았다고 말하고 싶은 거요?”

“그럼, 사내라면 원대한 목표를 세우고 나아갈 줄 알아야지.”

“그 원대한 목표라는 게 천하제일의 쟁자수는 아니었을 테고.”

“이 자식이 아까부터.”

발끈하는 석칠의 반응에 동료 쟁자수가 화제를 돌렸다.

“그런데 저 친구, 이름이 뭐요?”

“청풍(淸風).”

“아따, 이름 한번 멋있네. 잘 어울리기도 하고.”

“그건 그래.”

청년, 청풍을 내심 못마땅하게 생각하던 석칠이지만 그 말에는 십분 공감했다.

서글서글한 인상과 맑은 눈동자를 보고 있노라면 이상하게 마음이 편안해지고 화도 가라앉았다.

“이보게, 신참!”

동료 쟁자수의 말에 청풍이 고개를 돌렸다.

“저요?”

“그럼 여기 신참이 자네 말고 누가 있나? 이쪽으로 와서 불이나 좀 쬐게. 거기 앉아 있다가는 궁둥이가 뜯어져 나갈걸.”

“그런 경험도 나쁘지 않죠.”

“경험? 무슨 경험?”

“엉덩이가 뜯겨 나가는 경험이요. 제가 한 번도 그래 본 적이 없어서.”

잠깐 말이 없던 동료 쟁자수가 석칠에게 속삭였다.

“저거 뭐 하는 놈입니까?”

“몰라, 애가 좀 이상해. 뭘 잘못 먹었나 봐.”

청풍이 고개를 갸웃했다.

“아침에 만두 두 개 먹었는데요.”

“……귀가 밝구먼. 알았으니까 와서 앉기나 하게.”

“그럴까요?”

터벅터벅 걸어온 청풍이 모닥불 앞에 앉자 으레 하는 질문들이 날아들었다.

“어디서 왔나?”

“하남에서요.”

“하남 사람이었군.”

“한 달 전에는 호북에 있었고요.”

“음. 호북도 좋지.”

“그전에는…….”

쟁자수가 석칠에게 말했다.

“골 때리네.”

“그렇지? 이야기하다 보면 나까지 이상해지는 기분이라니까.”

“어떻게 이런 놈을 옆에 끼고 달포씩이나 버티셨소?”

“그래서 요즘 말 안 걸어. 마지막으로 대화한 게 사흘쯤 됐나?”

청풍이 진지한 얼굴로 대답했다.

“나흘 하고도 세 시진이요.”

“…….”

“…….”

두 사람은 청풍의 머리통을 한 대 쥐어박고 싶은 마음을 간신히 억눌렀다.

“그래서 어디 사람인가?”

“산에서 살았어요.”

“내 말은 그게 아니고…… 아닐세, 그거라도 대답해 줘서 고맙네.”

“별말씀을요.”

해맑게 웃는 청풍의 모습을 보니 신기하게도 화가 수그러든다.

종잡을 수 없는 엉뚱한 언행에 아이처럼 순수한 웃음. 난생처음 보는 별종에 관한 호기심이 이어졌다.

“한데, 산에서 살았다니?”

“말 그대로예요. 어릴 때부터 산에서 농사도 짓고, 약초도 캐고. 그 외에도 이것저것 하면서 살았거든요.”

두 사람은 청풍이 화전민 출신임을 지레짐작했다.

화전민 중 대부분은 악질 지주의 횡포를 못 견뎌서, 혹은 크고 작은 죄를 지어서 관의 눈을 피해 산으로 들어갔다.

“고생이 많았겠군.”

“전 재밌었는데요?”

“아, 그래?”

화전민 생활이 재미있을 수가 있나? 순간 석칠의 머릿속에 그런 생각이 스쳤지만, 굳이 물어볼 필요를 느끼진 못했다.

“그럼 하산(下山)하게 된 계기는 뭔가?”

“산속 생활이 심심해져서요. 세상 구경도 하고 싶고, 만나고 싶은 사람도 있었거든요.”

“그래서 하남에 온 거로군.”

“네. 어쩌다 보니 헛걸음을 하게 됐는데…… 지금도 나쁘지 않아요. 표행이란 것도 상당히 재밌어요.”

“표행이 재미있다고?”

청풍이 활짝 웃으며 대답했다.

“사람 구경하는 것도 재밌고, 땅도 보고, 하늘도 보고. 생각하는 것도 재밌어요.”

오랜 세월 쟁자수 일을 해 온 석칠에게는 이젠 지긋지긋한 광경이다.

피곤과 생계에 대한 고민으로 찌들어 있는 사람들, 축축한 땅과 미친 듯이 불어오는 칼바람. 머릿속엔 그저 이번 표행으로 얼마의 수당을 받을지만 꽉 차 있다.

‘하긴, 아직 젊으니까 할 수 있는 소리지.’

더군다나 평생 산에서 살아온 화전민 출신이니 그럴 법도 하다.

곧 냉정한 현실을 알게 되고 점차 나이를 먹으면 자신과 같은 모습이 되어 가지 않을까?

‘나도 저럴 때가 있었는데.’

석칠은 부러움과 안타까움이 섞인 눈빛으로 청풍을 바라보다가 입을 열었다.

“그냥 헛소리라고 생각하고 듣게.”

괜한 오지랖인 건 알지만, 이 순박한 청년에게 현실을 알려 주고 싶었다.

쟁자수로 시작해서 쟁자수로 늙어 죽기에는 너무 창창한 인생 아닌가.

“할 만한 것도 잠깐이야. 십 년, 이십 년쯤 되면 미래가 잘 보이지 않는다 이 말일세. 쟁자수는 아무리 날고 기어 봐야 쟁자수거든. 차라리 동네 무관(武關)에서 삼류 무공이라도 배워서 표사로 시작하게. 그편이 훨씬 나아.”

청풍은 눈을 깜빡였다.

“아, 그래요?”

“그래요, 가 아니고 그렇게 하란 소리야. 무공을 익히기에는 늦은 나이지만 혹시 아나? 의외로 무재가 뛰어나서 잘나가는 일류 고수가 될지.”

“일류 고수…….”

가만히 듣고 있던 동료 쟁자수가 혀를 찼다.

“거, 너무 헛바람 불어넣는 거 아니오? 일류 고수가 뉘 집 개 이름도 아니고.”

“말이 그렇다는 거야, 말이. 저 나이에 쟁자수로 만족한다는 게 말이 돼?”

“뭐, 그건 그렇죠. 나도 십 년만 젊었으면 여기서 안 이러고 있지.”

“거봐.”

석칠이 청풍의 어깨를 두드렸다.

“들었지? 일이 년만 알뜰하게 모아서 무관 등록 하는 게 훨씬 나아. 그때까진 내가 옆에서 잘 알려 줌세.”

청풍이 고개를 갸웃했다.

“일이 년이요?”

“왜, 너무 긴가? 자네가 세상 물정을 몰라서 그런가 본데, 무관비가 한두 푼 하는 게 아니야. 아무리 적게 잡아도 일 년은…….”

“아뇨, 제가 그 전에 관둘 거라서.”

“관둔다고? 언제?”

“지금이요.”

“응?”

“엥?”

청풍이 해맑게 웃었다.

“제가 산서성까지 가는 길을 몰라서요. 마침 산서로 가는 표행이 있길래 끼워 달라고 한 건데요.”

“……그래서?”

“이제 하루만 더 가면 태원(太元)이니까 이쯤에서 헤어지려고요.”

석칠과 동료 쟁자수는 이게 뭔가 싶은 얼굴로 서로를 마주 보았다.

“저놈 뭐야? 송 표두 말로는 일 년짜리 계약서에 수결(手決)했다고 하지 않았나?”

“나도 그렇게 알고 있소. 그러니까 최고참인 형님한테 배우라고 붙여 놓은 거였고.”

석칠이 혼란스러운 표정으로 청풍에게 물었다.

“자네, 하남에서 합류할 때 뭔가에 수결했었지?”

“앗, 네.”

“그거 갖고 있으면 줘 봐.”

청풍이 품에서 누리끼리한 죽간 하나를 꺼내어 보여 줬다.

앞으로 일 년간 성운표국에서 쟁자수로 일할 것이며, 도중 이탈 시 위약금을 문다는 내용의 계약서였다.

“글은 읽을 줄 알지?”

“네 살 때 사서삼경을 땠지요.”

“그딴 헛소리는 하지 말고. 거기 읽어 봐. 그래, 그 부분. 소리 내서 크게.”

청풍이 또랑또랑한 목소리로 석칠이 알려 준 부분을 읽어 내려갔다.

“수결 시 번복할 수 없으며, 무단이탈 시 은자 오십 냥의 위약금 혹은 그에 상응하는 대가를 치르게 될 것.”

“은자 오십 냥이 얼마인지는 알 테고. 그에 상응하는 대가라는 게 무슨 뜻인지 아나?”

곰곰이 생각에 잠겨 있던 청풍이 이마를 탁 쳤다.

“혹시 몸으로 때우라는?”

“그래, 이 멍청한 친구야. 표국이 무슨 무골호인들만 모여 있는 곳인 줄 알았어?”

석칠은 혈압이 올라 뒷덜미가 당겼다. 이놈의 머릿속에 뭐가 들어 있는지 정수리를 쪼개 보고 싶을 정도였다.

‘어떻게 이런 놈이 다 있지? 산에서만 살아서 그런가?’

천하를 가로지르며 물건을 운송할 때 겪는 위험은 상상을 초월한다. 마적, 수적, 산적, 온갖 도적 떼와 경쟁 표국의 견제까지.

행여 그 모든 장애물을 넘어도 자연재해 한 번 잘못 만나면 표행은 실패로 돌아간다.

어지간한 무림 문파만큼, 아니 그 이상으로 철저하고 거친 것이 표국이었다.

‘그런데 수결까지 찍어 놓고 뭐? 이쯤에서 헤어지겠습니다?’

눈앞의 이 젊은 놈은 세상을 몰라도 너무 모른다.

석칠은 애먼 목숨 구한다는 마음으로 입을 열었다.

“혹시나 해서 말해 두는데, 도망칠 생각은 일찌감치 접게. 그냥 일 년 동안 돈 번다 생각하고 일하란 말이야. 알겠나?”

“일 년은 너무 긴데요. 내일 하루까지는 일할 수 있을 것 같은데.”

“야, 이 새끼야!”

“형님, 형님 진정하십쇼! 괜히 송 표두가 보기라도 하면 피곤해져요.”

“놔! 안 놔?”

석칠의 눈이 뒤집힌 그때였다.

“어, 이 정도면 위약금으로 충분하지 않나요?”

쩔그럭.

청풍이 내민 손을 확인한 두 사람이 눈을 부릅떴다.

말발굽 모양의 그것은 눈보다 새하얀 은빛으로 번쩍거리고 있었다.

“은, 은원보(銀元寶)?”

“그것도 두 개나!”

은자 오십 냥에 해당하는 은원보가 무려 두 개.

은자 백 냥은 일개 쟁자수가 십 년간 뼈 빠지게 일해도 벌기 힘든 엄청난 거금이다.

그런 거금이 화전민 청년의 품에서 나올 줄이야.

“어, 어, 어, 어떻게.”

“집 나오면서 노잣돈을 좀 받았거든요.”

청풍의 천진난만한 대답에 두 사람은 입을 딱 벌렸다.

도대체 어느 집 자제길래 은자 백 냥을 노잣돈으로 준단 말인가. 심지어 소불알처럼 축 늘어진 전낭을 보니 저게 끝이 아닌 듯했다.

“일단 위약금은 이걸로 해결할 수 있을 것 같은데…….”

두 사람은 미친 듯이 고개를 끄덕였다.

“됩니다. 되고 말고요.”

“왜 갑자기 존댓말을 쓰세요?”

“그냥 이게 편해서 그럽니다.”

“맞습니다. 세상에서 제일 편합니다.”

“아, 그러시다면야 뭐.”

신기하다는 듯 두 사람을 바라본 청풍이 은원보 두 개를 건넸다.

“전 이만 가 볼게요. 이건 위약금이라고 전해 주세요.”

“이, 이걸 다 말입니까?”

“너무 많은데…….”

“남으면 두 분이 나눠 쓰세요. 제가 돈 쓰는 법을 잘 몰라서. 따뜻한 옷이라도 하나씩 사 입으세요. 비싼 털가죽 달린 걸로.”

“……!”

주섬주섬 봇짐 하나를 둘러메고 떠나려는 청풍의 모습에 석칠이 황급히 입을 열었다.

“호, 혹시 성함이?”

“청풍이요. 보름 전까지는 하남 사람이었고, 지난달에는 호북, 그전에는 섬서에 살았죠.”

대답을 마친 청풍은 태원을 향해 성큼성큼 걷기 시작했다.

하늘을 푸르렀고, 축축한 땅 위로는 때 이른 새싹이 돋아나고 있었다.

“이번 봄은 좀 일찍 오려나?”

그는 활짝 웃으며 생각했다. 이번 봄에도 매화가 흐드러지게 피었으면 좋겠다고.

문득 얼마 전 몰래 뛰쳐나온 화산(華山)의 연화봉(蓮花峰)이 생각났다.
```

## Final English reading copy

```markdown
# Chapter 130

Winter in the borderlands was harsh. A middle-aged man shivered violently as the knife-sharp wind cut through his collar.

“Ugh, it’s cold as hell.”

The man, Seokchil, was a porter for the Seongun Escort Bureau in southern Shanxi Province.

He had spent more than a day and a half hauling a cart loaded with over a hundred geun of cargo, soaking his entire body in sweat. Whenever he took a brief rest, as he was now, he had to fight against the brutal cold.

“Hyung, hurry up and leave the cart. Come warm yourself by the fire before you freeze to death.”

A fellow porter, already crouched in front of the campfire, called out. Seokchil answered gruffly as he walked over.

“Brat, I have five mouths to feed. I’ve got a long way to go before I’m ready to die.”

“True. You can’t die when you’ve got a fox of a wife and rabbit-like children waiting for you.”

“What do you mean, fox? She’s a bear. A bear.”

“Was that a deathbed confession? If your wife hears you, she’ll wring your neck.”

“You can curse the king behind his back. What, you didn’t know that?”

Seokchil moved closer to the campfire.

They used horse manure for firewood, so a foul smell spread in every direction. But after nearly twenty years as a porter, Seokchil was as used to it as he was to the smell of cooking rice.

“Ah, now I feel like I can live again.”

“But Hyung, aren’t you being a little stingy?”

“Huh? What kind of nonsense is this?”

His fellow porter grinned and jerked his chin toward something.

“You should bring the rookie over, too. Where’s the sense in rushing over here to save yourself alone?”

Seokchil, who had been warming his frozen hands, turned his head. At the end of his gaze sat a young man on a snow-covered rock, staring blankly into space.

*That kid’s doing it again.*

The young man was a new porter they had picked up in Henan. Escort Chief Song, the person in charge of this escort run, had said that the young man seemed capable enough to earn his keep, so they had taken him on.

*Well, people are always in short supply.*

The problem was that the young man often sat around like this, completely lost in thought, and no one had the slightest idea what was going on inside his head.

As Seokchil clicked his tongue, his fellow porter asked,

“Why? Is he a little strange?”

“He does his work well. He’s surprisingly strong for someone who doesn’t look like much.”

“Then what’s the problem?”

“What do you mean, what’s the problem? It’s frustrating seeing a young fellow sit around like that every day. Back when I was his age…”

“You want to say you had dreams of making your mark on the world and worked hard every day?”

“Of course. A man should know how to set a grand goal and move toward it.”

“I assume that grand goal wasn’t becoming the greatest porter under heaven.”

“You little—”

At Seokchil’s furious reaction, his fellow porter quickly changed the subject.

“By the way, what’s that fellow’s name?”

“Cheongpung.”

“Wow, what a great name. It suits him, too.”

“That’s true.”

Seokchil secretly disliked the young man, Cheongpung, but he had to agree completely.

There was something about the young man’s open, gentle features and clear eyes that made people feel strangely at ease and calmed their anger.

“Hey, rookie!”

At his fellow porter’s shout, Cheongpung turned his head.

“Me?”

“Who else would I be talking to? Come over here and warm yourself by the fire. If you keep sitting there, your butt will get ripped right off.”

“An experience like that wouldn’t be bad.”

“An experience? What experience?”

“The experience of having my butt ripped off. I’ve never had that happen before.”

His fellow porter was silent for a moment before whispering to Seokchil,

“What kind of guy is he?”

“I don’t know. The kid’s a little strange. Maybe he ate something bad.”

Cheongpung tilted his head.

“I ate two dumplings this morning.”

“……You’ve got sharp ears. Fine, just come sit down.”

“Should I?”

Cheongpung trudged over and sat down in front of the fire. The usual questions immediately began flying at him.

“Where are you from?”

“Henan.”

“So you’re from Henan.”

“I was in Hubei a month ago.”

“Hmm. Hubei’s nice, too.”

“Before that…”

The porter turned to Seokchil.

“This guy’s unbelievable.”

“Right? I feel like I’m becoming strange myself whenever I talk to him.”

“How have you lasted over a month with someone like him beside you?”

“That’s why I stopped talking to him lately. Has it been about three days since our last conversation?”

Cheongpung answered with a serious expression.

“Four days and three shichen.”

“……”

“……”

The two men barely managed to suppress their urge to smack Cheongpung over the head.

“So where are you from?”

“I lived in the mountains.”

“That’s not what I meant… No, never mind. Thank you for answering that, at least.”

“You’re welcome.”

Strangely, Cheongpung’s bright smile made their anger subside.

His unpredictable, bizarre remarks were paired with an innocent smile like a child’s. Their curiosity about this strange young man, unlike anyone they had ever seen, continued to grow.

“But you said you lived in the mountains?”

“I mean exactly what I said. I farmed and gathered medicinal herbs in the mountains from the time I was young. I did various other things, too.”

The two men jumped to the conclusion that Cheongpung was from a slash-and-burn farming community.

Most slash-and-burn farmers went into the mountains to escape the cruelty of vicious landlords or to avoid the authorities after committing one crime or another.

“You must have had a hard life.”

“But I had fun.”

“Oh, really?”

Could life as a slash-and-burn farmer really be fun? The thought briefly crossed Seokchil’s mind, but he saw no reason to ask.

“Then what made you come down from the mountain?”

“Life in the mountains got boring. I wanted to see the world, and there were people I wanted to meet.”

“So that’s why you came to Henan.”

“Yes. It turned out to be a wasted trip, but… things aren’t bad now, either. This escort work is pretty interesting, too.”

“You find escort work interesting?”

Cheongpung answered with a broad smile.

“Watching people is interesting. Looking at the land and the sky is interesting, too. Thinking is fun.”

To Seokchil, who had worked as a porter for so many years, these were all sights he was sick to death of seeing.

People worn down by exhaustion and worries about making a living. Damp earth and knife-sharp winds that blew like mad. His mind was filled with only one thought: how much pay he would receive for this escort run.

*Well, he’s still young. That’s the only reason he can say something like that.*

Besides, he had lived in the mountains his entire life and came from a slash-and-burn farming community. It made sense that he would feel this way.

Wouldn’t he learn about the harsh realities of life soon enough and gradually become just like Seokchil as he grew older?

*I used to be like that, too.*

Seokchil looked at Cheongpung with a mixture of envy and pity before opening his mouth.

“Just listen to this as the ramblings of an old man.”

He knew he was meddling where he wasn’t wanted, but he wanted to show this innocent young man the realities of life.

Wasn’t his life too promising to begin and end as a porter?

“Anything seems worthwhile for a while. But after ten or twenty years, you stop seeing much of a future ahead of you. No matter how hard a porter works or how talented he is, he’s still a porter. You should learn even Third Rate martial arts at a local martial arts academy and start working as an escort. You’d be much better off.”

Cheongpung blinked.

“Oh, really?”

“Not ‘oh, really?’ I’m telling you to do it. You’re a little old to start learning martial arts, but who knows? Maybe you have exceptional talent and could become a successful First Rate master.”

“A First Rate master…”

His fellow porter, who had been listening quietly, clicked his tongue.

“Isn’t that giving him too much false hope? A First Rate master isn’t some dog’s name.”

“I’m speaking hypothetically. What kind of sense does it make for someone his age to be satisfied with being a porter?”

“Well, you’re right about that. If I were ten years younger, I wouldn’t be sitting here either.”

“See?”

Seokchil patted Cheongpung on the shoulder.

“You heard him, right? Save carefully for a year or two and enroll in a martial arts academy. It’ll be much better for you. Until then, I’ll teach you everything I know.”

Cheongpung tilted his head.

“A year or two?”

“What? Is that too long? You don’t know how the world works, so I suppose you don’t realize that martial arts academy fees aren’t cheap. Even if you take the lowest estimate, it’ll take a year to…”

“No, because I’m going to quit before then.”

“You’re quitting? When?”

“Now.”

“Huh?”

“What?”

Cheongpung smiled brightly.

“I don’t know the way to Shanxi Province. There happened to be an escort run heading to Shanxi, so I asked them to let me tag along.”

“……And?”

“We’ll reach Taiyuan after one more day, so I was planning to part ways around then.”

Seokchil and his fellow porter looked at each other with expressions that seemed to ask whether this was some kind of joke.

“What the hell? Didn’t Escort Chief Song say he signed a one-year contract?”

“That’s what I heard, too. That’s why they assigned him to the most experienced porter, so he could learn from him.”

With a confused expression, Seokchil asked Cheongpung,

“When you joined us in Henan, you signed something, didn’t you?”

“Oh, yes.”

“If you have it, show it to me.”

Cheongpung pulled a yellowish bamboo slip from inside his clothes and showed it to them.

It was a contract stating that he would work as a porter for the Seongun Escort Bureau for one year and pay a penalty if he left before then.

“You can read, right?”

“I finished studying the Four Books and Three Classics when I was four.[^1]”

“Don’t say stupid things like that. Read this part. Yes, that section. Read it aloud, and make sure I can hear you.”

In a clear voice, Cheongpung read the section Seokchil pointed out.

“Once signed, this contract cannot be revoked. In the event of unauthorized departure, the signer shall pay a penalty of fifty nyang of silver or provide compensation of equivalent value.”

“You know how much fifty nyang of silver is, right? Do you know what ‘compensation of equivalent value’ means?”

Cheongpung thought deeply for a moment, then slapped his forehead.

“Does it mean I’d have to work it off?”

“That’s right, you idiot. Did you think the Escort Bureau was full of nothing but kindhearted saints?”

Seokchil’s blood pressure rose, and the back of his neck began to ache. He wanted to split the top of this kid’s skull open and see what was inside.

*How can someone like this even exist? Is it because he only ever lived in the mountains?*

The dangers of transporting goods across the land were beyond imagination. Mounted bandits, river bandits, mountain bandits, every kind of bandit gang imaginable, not to mention interference from competing Escort Bureaus.

Even if they overcame all those obstacles, one encounter with a natural disaster could bring an escort run to failure.

An Escort Bureau was every bit as thorough and hard-edged as most Murim sects, if not more so.

*And this kid signed the contract, then says what? “I’m leaving around here”?*

The young fool in front of him knew far too little about the world.

Seokchil spoke, determined to keep the boy from throwing his life away.

“I’m telling you this just in case, so give up on running away right now. Work for a year and think of it as earning money. Understand?”

“A year is too long. I think I can work until tomorrow, though.”

“You little bastard!”

“Hyung, Hyung, calm down! If Escort Chief Song happens to see this, we’ll all be in trouble.”

“Let go! I said let go!”

It was just then, as Seokchil was about to snap.

“Uh, wouldn’t this be enough to cover the penalty?”

Clink.

The two men’s eyes widened when they saw what Cheongpung held out.

The object was shaped like a horse’s hoof and gleamed with a silver light whiter than the snow.

“Is that a silver ingot?”

“And there are two of them!”

There were two silver ingots, each worth fifty nyang of silver.

A hundred nyang of silver was an enormous sum that an ordinary porter would struggle to earn even after working himself to the bone for ten years.

And yet such a fortune had come from the clothes of a young man from a slash-and-burn farming community.

“H-how?”

“I was given some traveling money when I left home.”

At Cheongpung’s innocent answer, both men’s mouths fell open.

What kind of family gave their son a hundred nyang of silver as traveling money? And judging from the money pouch hanging limp like a bull’s testicles, this didn’t seem to be all he had.

“At least it looks like the penalty can be settled with this…”

The two men nodded frantically.

“It can. Of course it can.”

“Why did you suddenly start speaking formally?”

“It’s just more comfortable this way.”

“Exactly. It’s the most comfortable thing in the world.”

“Oh. If that’s what you prefer.”

Cheongpung looked at the two men as if they were strange and handed over the two silver ingots.

“I’ll be going, then. Please tell them this is the penalty.”

“A-are you really giving us both?”

“It’s too much…”

“If there’s any left over, you two can split it. I don’t really know how to spend money. Buy yourselves some warm clothes. Something with expensive fur on it.”

“……!”

As Cheongpung slung a bundle over his shoulder and prepared to leave, Seokchil hurriedly spoke.

“C-could I ask your name?”

“Cheongpung. Until half a month ago, I was from Henan. Last month, I lived in Hubei, and before that, I was in Shaanxi.”

After answering, Cheongpung began walking steadily toward Taiyuan.

The sky was blue, and early shoots were already sprouting from the damp earth.

“Maybe spring will come a little early this year.”

He smiled brightly as he thought about it. He hoped the plum blossoms would bloom in profusion again this spring.

Then, without warning, he thought of Lotus Peak on Huashan, from which he had secretly run away not long ago.

[^1]: The Four Books and Three Classics are foundational Confucian texts.
```
