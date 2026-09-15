<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0111.txt",
      "sha256": "16999412d470772f613e9c26859b0b1c067a7f3573162408460d6625d6c9ff98",
      "bytes": 13806
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "51a9578be85fa3a571ba17c01e54d6f40d6971fea3649bd53b75633812a40836",
      "bytes": 4439
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91a80f7ac9d6d447e9b10bd1bd85b6054eeadc71d2abe93d8ac25ba7f5448203",
      "bytes": 15760
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "366558de06d44c8ac04a300afd498983718f9127b53b0cfbec4e2aef97455fb6",
      "bytes": 724
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "14bdb771ec802c9a0b73cebd8a8fcbca3ba19ecf1d4bb6db0134e7bb74eb49df",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "4a9e0f77a1f7bf9ad95530b6583ee280664d3f9ef2e73920ef4bb3d19aea43a2",
      "bytes": 1221
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4a813187d306a48fe38233837b3cf1b53d3e16c8912599047d5efd83a37115e2",
      "bytes": 24117
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "c9c720611fe8e723d6052db8973a4e128432f3876f7991e9434baef0fd7dd5b4",
      "bytes": 3149
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "0793eb44e28cce877546b4e4d59bc13a73085a403ff356e863bc93879296f3f3",
      "bytes": 720
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "402e83af14201ceb313b88793918766262e28cf72a53bdb1862386c28c3bee57",
      "bytes": 563
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "5acba09c3fb2902d3fe0c21954ed349c71983b63a589af1579f0764bf48ce3d4",
      "bytes": 2314
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "079f31258d8a35d65fc2c0ca7a78d698dae5ec85bd69b4f56c2f9b1dc7a8f7cc",
      "bytes": 15617
    }
  ],
  "estimated_tokens": 19046
}
-->

# Durable State Update — Chapter 111

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 111. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 111. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 111,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 111,
    "continuity_sources": [111],
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
    "Taekyung, Mukyung, Mujin, and Wolhwa are riding toward the Mount Heng Sword Sect.",
    "The Five-Colored Ghosts and surviving mounted bandits are being taken to a nearby Lower District Sect branch.",
    "A messenger hawk from the Lower District Sect's Sakju Branch delivered intelligence to Wolhwa.",
    "The Red Wind Band is moving south with approximately two hundred members.",
    "The Red Wind Band has crossed Datong and destroyed the Mount Heng Sword Sect's Datong Branch with no survivors.",
    "Pung Yang is the Red Wind Band Leader and commands his force with ruthless authority.",
    "Chunsam is a First Rate Lower District Sect martial artist who served as the group's carriage driver.",
    "Wolhwa uses lethal interrogation to obtain information from hostile mounted bandits.",
    "The Mount Heng Sword Sect has lost nearly eighty percent of its strength in the war with the Jin Family of Taiyuan.",
    "The Mount Heng Sword Sect's main hall doors have exploded as the attack begins.",
    "The Quest concerning the Mount Heng Sword Sect is graded Peak and requires Taekyung to deliver an invitation to the Jin Family during the upcoming Lunar New Year.",
    "Cheol Mubaek is a Peak master known as the Tiger of Mount Heng and a close friend and peer of Lee Cheonbaek.",
    "Cheol Mubaek's Scorching Yang Qi can make nearby people struggle to breathe, but he can suppress it at Lee Seowol's request.",
    "Lee Seowol is the current Sect Leader of the Mount Heng Sword Sect and insists on being addressed by that title rather than Young Lady.",
    "Cheol Mubaek is Lee Seowol's paternal uncle and protector.",
    "The Quest requires Taekyung to reach the Mount Heng Sword Sect within 22 hours; being late is stated to be irreversible.",
    "Taekyung is Level 55, and Hyuk Mujin is Level 38 after rising from Level 20 over roughly two months.",
    "The party's horses are exhausted after a forced march and require a one-hour rest."
  ],
  "continuity_sources": [
    110
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation remains unknown.",
    "Why Kim Hwajong now works as a butler despite his former instructor status and exceptional ability remains unexplained.",
    "What final disciplinary action will be taken against the Security Team remains unknown.",
    "How and why Seong Jinho entered the capsule and emerged inside Taekyung's new house remains unknown.",
    "How Lee Seowol and Mount Heng will respond to the merger proposal, and what compensation or territorial concession Wolhwa will receive, remain unresolved.",
    "What final outcome will follow Cheol Mubaek and Lee Seowol's assertion of authority inside the damaged main hall remains unresolved."
  ],
  "safe_through": 110,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술 and keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you; 김화종's 춘수 and 교관님 as Chunsoo and Instructor; 1번 훈련생 as Trainee Number One; and 열양공 as heat-yang technique.",
    "Render 원단 as Lunar New Year; 봉황객잔 as Phoenix Inn; 계용옥미갱 and 계용옥미앵 as chicken-and-corn soup; and 곡도 as curved saber.",
    "Render 마적 and 마적단 as mounted bandits and mounted-bandit groups; 적풍단 as Red Wind Band; 적풍단주 as Red Wind Band Leader; and 토호단 as Earth Tiger Band.",
    "Render 초일류 as master beyond First Rate; preserve Wolhwa's Young Master forms for Taekyung and Young Hero Jin for Mukyung; render 관제묘 as Guandi Temple and 흑도 as dark-path figures; render 소월 as Seowol and 철 숙부 as Uncle Cheol.",
    "Render 오색귀 as Five-Colored Ghosts, 이삼 as Lee Sam, 전서응 as messenger hawk, and 대형 as Boss.",
    "Render 추종향 as tracking scent, 대동 as Datong, 풍양 as Pung Yang, 춘삼 as Chunsam, 철검대주 as Iron Sword Squad Leader, 대항산검문 as great Mount Heng Sword Sect, and 대동지부 as Datong Branch.",
    "Render 절정 as Peak, 일류 as First Rate, 일격 as One Strike, 단주 as Leader, 아가씨 as Young Lady, 문주님 as Sect Leader, and 반 시진 as one hour."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소광    | **Lee Seogwang**   |
| 이소군    | **Lee Seogeun**    |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 일신     | **One God**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 은인     | **Benefactor**                               |
| 퀘스트              | **Quest**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 본문      | **our sect / this sect**                                        |
| 공자      | **Young Master**                                                |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 정양 | **Jeongyang** | Shanxi location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 110
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 110
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 110
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 110
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 110
- **Aliases:** Blood Wolf Sword
- **Role:** Sect Leader of the Mount Heng Sword Sect; Lee Seogeun’s father
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; leader of the Mount Heng Sword Sect; longtime close friend and peer of Cheol Mubaek

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 110
- **Aliases:** None
- **Role:** Current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Lee Cheonbaek's daughter; younger sister of the deceased Young Sect Leader and Lee Seogeun; Cheol Mubaek's niece and protected charge

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 109
- **Aliases:** Red Wind Band Leader
- **Role:** Leader of the Red Wind Band; commands a force of at least two hundred mounted bandits
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 110
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃111화



두두두두!

네 마리 준마가 관도를 내달린다. 휴식이 부족했던 탓에 지칠 대로 지친 말들이 숨을 헐떡거렸지만 고삐를 늦출 수 없었다.



제한 시간 : 16:25:32



31, 30. 시간은 계속해서 줄어들고 있다.

벌써 세 시진, 자그마치 여섯 시간이 흘렀다. 오는 길에 작은 마을에 들러 갈아탈 말을 구하려 했지만 작고 느려 터진 짐말밖에 없었다.

‘휴식을 취하긴 해야 하는데.’

외통수다.

충분히 강행군을 이어 가고 있지만 제한 시간이 아슬아슬하고, 지금처럼 달리면 말이 버티지 못할 거다.

‘어쩔 수 없나.’

월화와 진무경에게 잠시라도 쉬어 가자고 말하려던 찰나였다.

“어?”

“진 공자! 앞에!”

굳이 월화의 외침이 아니더라도 나는 이미 놈들을 보고 있었다. 수십 장 앞, 관도를 막아선 시커먼 사내들.

하나같이 너저분한 옷차림에 허리춤에는 곡도 한 자루가 삐죽 튀어나와 있다. 이제 두말하면 입 아프다.

‘적풍단.’

양민으로 보이는 이들을 빙 둘러싸고 으름장을 놓던 놈들이 말발굽 소리에 고개를 홱 돌렸다.

멀찍이 선두에서 앞서 달리던 나를 발견한 마적들이 누런 이를 드러내며 웃는다.

“어이구, 벌써 다음 손님 오셨네. 정지!”

“어, 그래.”

멈추라는데 멈춰야지, 별수 있나.

퍼버벅!

“커허어억!”

“끄악!”

내가 타고 있는 준마는 앞을 가로막고 있던 두어 놈을 짓밟고 나서야 멈췄다. 마적들은 물론이고 붙잡혀 있던 행인들까지 눈을 동그랗게 뜨고 날 쳐다본다.

“너, 너 이 새끼!”

안장에서 훌쩍 뛰어내리며 물었다.

“혹시 몰라서 물어본다. 적풍단, 맞지?”

“웬 놈이냐!”

“반응 보니까 맞나 보네. 시간 없으니까 빨리 끝내자.”

망설임 없이 가장 가까이 있는 놈의 다리를 걷어찼다.

콰직, 섬뜩한 소리와 함께 정강이뼈가 부러진 놈이 주저앉는다.

창졸간에 벌어진 일. 순간 얼이 빠져 있던 놈들이 재빨리 곡도와 창을 들이댔다.

“죽여!”

“남자는 항상 후방을 주의해라.”

“뭐?”

“뒤에 조심하라고.”

열 쌍의 눈이 내 말이 끝나자마자 등 뒤를 돌아보던 그때.

콰드드득! 뻐억!

전속력으로 달려온 세 마리의 준마가 놈들을 쓸어 버렸다.



* * *



전투는 시작되기도 전에 끝났다. 말에 치여 볼링 핀처럼 나가떨어진 놈들은 산송장처럼 누워 있었고 나머지 놈들도 손쉽게 제압당했다.

“사, 살려만 주십시오.”

“안 죽인다. 몇 군데는 손봐 줘야겠지만.”

“히익!”

진무경이 살아남은 산적들의 팔다리를 똑똑 분지르는 사이 혁무진은 길옆에 매여 있던 말들을 끌고 왔다.

“여기 팔팔한 놈들로 갈아타면 될 것 같은데요? 열 마리는 되니까 아예 싹 가져가서 지칠 때마다 교체하고.”

나도 같은 생각이다. 지난번 놈들과는 달리 이번에 만난 마적들은 각자 말을 소지하고 있어서 다행이었다.

‘그나저나…….’

이놈의 적풍단 놈들은 도대체 몇 명이나 있는 거야?

사당에서 얻은 정보에 의하면 백 명이 넘는 잔당들이 산서 북부 곳곳으로 흩어졌다고 했다.

더러는 산자락으로, 더러는 궁벽한 마을 혹은 번화한 곳에서 숨어 있다가 명령에 따라 집결지로 모인다는 것이다.

‘이놈들, 패잔병이 아니야.’

놈들은 작전을 수행 중인 복병이다. 적풍단주는 고원에서 병력을 충원하여 남하(南下)하는 한편 남겨 둔 수하들을 북상(北上)시키고 있다.

월화가 적풍단주를 무서운 인물이라고 평한 이유를 충분히 짐작하고도 남는다.

‘전황이 불리하게 흘러가니 신속하게 물러나는 판단력, 그 와중에도 다음 계획을 준비하는 치밀함, 그리고 계획을 실행시키는 추진력.’

거기에 더해 그는 일신에 지닌 무공도 고강하다고 들었다.

이쯤 되면 단순한 마적 취급하기도 미안할 지경이다.

‘이거 일이 상당히 지저분하게 됐는데.’

왜 퀘스트 등급이 절정으로 바뀌었는지 알겠다. 점입가경으로 알고 보니까 뭐, 적풍단주가 절정 고수라든지 그런 건 아니겠지?

혹시나 하는 마음에 월화에게 물었더니 대번에 고개를 끄덕인다.

“네. 맞는데요?”

“……아.”

“이렇게 급속도로 두각을 드러낸 것에는 이유가 있기 마련이죠. 아직 널리 알려지지는 않았지만 본 문의 정보에 의하면 적풍단주는 절정 고수가 맞아요.”

나는 어이가 없어져서 물었다.

“아니, 절정 고수가 왜 마적질을 합니까?”

“산적, 수적 중에서는 초절정 고수도 있는데 마적이라고 못 할 것 있나요.”

“초절정 고수요? 산적, 수적이?”

“나중에 녹림맹주나 장강수로맹주를 만나면 물어보세요. 그럴 일은 없겠지만.”

“……제발 그랬으면 좋겠네요.”

초절정 고수라니, 진심으로 만나는 일이 없었으면 좋겠다.

고개를 절레절레 흔들고 새로 뺏은 말에 올라탔다. 적풍단의 마적들을 꽁꽁 묶어 양민들에게 넘긴 진무경과 혁무진이 그 뒤를 잇는다.



제한 시간: 15:59:13



이 순간에도 제한 시간은 흘러가는 중이다. 우리는 허리 숙여 감사를 표하는 양민들을 뒤로하고 말 옆구리를 걷어찼다.

“이랴!”



* * *



항산검문 깊숙한 내원에는 극소수의 사람들만 드나들 수 있는 화원이 존재한다. 항산호 철무백은 외부인 중 유일하게 그 자격을 부여받은 사람이었다.

“이곳에 온 것은 이번이 처음이구나.”

“특별한 공간이었으니까요. 아버지는 고민이 있으실 때마다 화원을 찾으셨죠.”

눈 덮인 화원을 사박사박 걷던 이소월이 서리 낀 꽃 한 송이를 발견하고 문득 걸음을 멈췄다.

“어머니가 좋아하시던 꽃이에요.”

“그랬느냐?”

“네, 화원을 가꿀 때면 항상 저를 이곳으로 데려와서 꽃의 이름을 알려 주시곤 했죠.”

잠시 곰곰이 생각에 잠겨 있던 이소월이 말을 이었다.

“그런데 지금은 기억이 안 나네요.”

“오래전 일이니 그럴 만하다. 괘념치 말거라.”

“철 숙부.”

“응?”

“저, 꽃 싫어해요. 어머니가 좋아서 따라왔을 뿐이지, 사실 꽃에는 관심도 없었어요. 아버지께서 화원을 찾으시는 이유와 같은 거죠.”

이소월은 눈 덮인 화원을 천천히 둘러보았다. 꽃은 시들었고 화원 중앙에 마련된 봉분(封墳)은 하나에서 넷으로 늘었다.

가족들이 잠들어 있는 봉분을 말없이 바라보는 그녀의 눈빛이 깊게 가라앉았다.

‘누구의 잘못일까?’

어쩌면 무림인의 딸로 태어난 자신의 잘못일지도 모르겠다.

그것이 십 년 전 어머니에 이어 아버지와 두 오라버니를 차례로 잃어야 했던 이유다.

‘끝까지 말렸어야 했는데…….’

문득 두 달 전의 기억이 떠올라 눈 앞을 가린다.

그건 어느 야심한 밤, 단둘이 나눴던 부녀(父女) 간의 대화였다.



‘널 태원진가의 셋째와 엮어야겠다.’

‘셋째라면. 설마 그 망나니와 절 맺어 줄 생각이신가요?’

‘아니다. 그러나 너로서는 견디기 힘든 추문(醜聞)이 될 것이다.’

‘그렇군요.’

‘그뿐이냐?’

‘어쩌겠어요. 비정한 아비를 둔 제 잘못이죠.’

‘알다가도 모를 아이구나. 정말 아무렇지 않은 게냐?’

‘제가 싫다고 하면, 마음을 돌리실 건가요?’

‘적어도 다른 방법을 찾아보겠지.’

‘결국 태원진가와의 전쟁은 기정사실이군요.’

‘산서괴협(山西怪俠)과 진천검이 없는 지금이 적기다. 두 번 다시 오지 않을 기회야.’

‘가주와 이공자가 없어도 태원진가는 강해요. 부디 재고를.’

‘불가(不可). 결정은 이미 내렸다.’

‘그렇다면 반드시 승리하세요. 산서 땅에서 저에 관한 추문 따위는 입도 벙긋 못 할 정도로 강해지세요.’

‘……네가 사내였다면 소문주로 삼았을 것이다.’

‘여인으로 태어나서 다행이네요. 본문의 소문주 따위, 관심도 없으니.’



우려는 얼마 지나지 않아 현실로 바뀌었다.

보름이나 지났을까, 이소군이 싸늘한 시신으로 돌아왔다. 그리고 얼마 후에는 이천백이, 결국은 큰 오라버니인 이소광마저 잃고 말았다.

‘이제는 나 혼자야.’

그렇게 혈랑검 이천백의 마지막 남은 혈육은 새로운 문주가 되었다.

말없이 봉분을 응시하는 이소월의 어깨를 따뜻한 손바닥이 조심스레 어루만졌다.

“미안하구나. 내가 더 빨리 왔어야 했는데…….”

“철 숙부, 그런 말씀 마세요. 숙부께서 와 주시지 않았다면 본 문은 지금까지 버티지도 못했을 테니까.”

적풍단의 거친 공세에 항산검문은 속절없이 밀리는 중이었다. 뒤늦게 이천백의 변고를 접하고 달려온 항산호라는 절정 고수가 없었다면 적들이 물러나는 일도 없었을 것이다.

“내 반드시 그놈의 사지를 찢어 죽일 것이다.”

적풍단주를 떠올린 이소월은 고개를 저었다.

절정 고수끼리의 생사결이라면 철무백이 한 수 앞선다.

이미 앞서 한 번의 격돌이 있었고 풍양은 가벼운 내상과 함께 물러난 전적이 있다.

‘하지만 두 번 다시 그런 기회는 오지 않아.’

항산검문은 북쪽 고원의 마적들에 관해 늘 정보를 수집하고 촉각을 곤두세우고 있었다.

고원에 존재하는 마적단은 수십 개지만 그중에서도 풍양이 이끄는 적풍단은 눈에 띌 정도로 무섭게 성장했다.

고원의 우두머리 중에서도 특히 강하고 치밀한 자. 그가 바로 풍양이다.

‘그런 자가 철 숙부와 생사결을 펼칠 리 없어. 섣불리 상대하려 했다가는 거꾸로 당하고 말 거야.’

이소월은 철무백을 향해 고개를 돌렸다.

“철 숙부. 풍양의 무공에 대해 다시 한번 말씀해 주실 수 있나요?”

“절정 초입. 도법과 비도술이 경지에 오른 자였다. 다만.”

철무백의 미간에 깊은 골이 파였다.

“초식 하나하나가 음험하기 짝이 없더구나. 아마 사마외도(邪魔外道)의 무공을 익힌 듯싶었다.”

“사마외도…….”

정마대전 이후 중원에서 사마외도는 곧 죽음이라는 단어와 동일시되었다. 정파를 표방하는 사파는 있을지언정, 당당히 사파라고 외치는 이들은 없다.

“아직까지는 짐작일 뿐이다. 다시 한번 붙어 보면 알게 되겠지.”

“철 숙부를 믿어요. 그러나 적풍단주를 우습게 보진 마세요. 그에게는 목숨을 대신할 수하들이 얼마든지 있으니까.”

위아래로 짓쳐 드는 적들을 합하면 삼백에 가까운 대병력.

반면 항산검문은 각 지부에 나가 있는 무인들까지 모두 끌어모았음에도 그 절반에도 못 미친다.

상황이 이렇다 보니 일반 무인들은 물론이고 새로 임명된 중진들의 사기도 저조했다.

“소월아. 내 한마디 해도 되겠느냐?”

죽은 벗과의 우정을 위해 자신의 목숨을 건 은인의 말이다. 이소월은 공손히 고개를 숙였다.

“새겨듣겠습니다.”

철무백이 무겁게 입을 뗐다.

“떠나거라.”

많은 의미가 담겨 있는 한마디.

그러나 이소월의 대답에는 한 치의 망설임도 없었다.

“죄송합니다.”

“아직 늦지 않았다. 넌 살아남아야 한다.”

“아직 끝나지 않았습니다. 살아남을 거고요.”

“천백이 그 친구가 이런 걸 원한다고 생각했다면…….”

“숙부님.”

단호한 목소리에 철무백이 입을 다물었다. 이소월의 맑은 눈동자엔 굳은 결의가 어려 있었다.

“제가 원한 겁니다. 항산검문의 문주로서.”

“휴우…….”

철무백은 대답 대신 한숨을 토해 냈다.

“숙부께는 이미 많은 신세를 졌습니다. 이대로 떠나신다고 해도 원망하지 않을 거예요.”

“굳이 내 대답을 들어야 직성이 풀리겠느냐?”

이소월은 고개를 저었다. 어릴 적부터 그녀를 자식처럼 아껴 주었던 철무백이다. 오히려 아버지보다 더 아버지 같은 사람이기도 했다.

“이 은혜는 결코 잊지 않겠습니다. 철 숙부는 저와 항산검문의 은인이십니다.”

“어려서부터 봤지만…… 너는 참 영악한 아이다.”

“어릴 때는 영악했고, 지금은 독한 년이죠.”

싱긋 웃는 이소월을 보며 철무백은 연신 깊은 한숨만 내쉬었다.

“승산은 있는 게냐?”

“지금이라면 일 할.”

“뭐라?”

“하지만 지원군이 도착한다면 오 할. 그 이상이죠.”

“지원군이라니, 혹시 태원진가에서?”

“두 시진 전에 하오문 정양 지부에서 보낸 전서구가 도착했어요.”

“얼마나 된다 하더냐? 백? 이백?”

“넷이요. 그중 하나는 진천검 진무경이고, 다른 하나는…….”

이소월이 실소를 흘렸다. 그와 얽힌 악연이 생각나서다.

“산서잠룡 진태경.”
```

## Final English reading copy

```markdown
# Chapter 111

*Thudthudthudthud!*

Four fine horses raced down the main road. Exhausted from their lack of rest, the horses were already gasping for breath, but there was no way we could loosen the reins.

> **System**
>
> **Time Limit:** 16:25:32

31, 30. The time kept ticking down.

Three *sijin*—six hours—had already passed. We had tried to stop at a small village along the way and find fresh horses, but all they had were small, painfully slow packhorses.

*We really do need to rest.*

We were trapped between a rock and a hard place.

We had been forcing our march as hard as we could, but the time limit was dangerously close. If we kept running like this, the horses wouldn’t hold out.

*Can’t be helped.*

I was just about to suggest to Wolhwa and Jin Mukyung that we rest, even if only briefly, when—

“Hm?”

“Young Master Jin! Ahead!”

Even without Wolhwa’s shout, I had already seen them. Several dozen *jang* ahead, a group of dark figures blocked the main road.

Every one of them wore filthy clothes, with a single curved saber sticking out from his belt. There was no need to say anything more.

*The Red Wind Band.*

The men had surrounded what appeared to be ordinary civilians and were threatening them. At the sound of hoofbeats, they whipped their heads around.

The mounted bandits spotted me riding well out in front and grinned, baring their yellow teeth.

“Well, look at that. Our next customers have already arrived. Stop!”

“Oh, sure.”

They told me to stop, so I had to stop. What else could I do?

*Thud! Thud!*

“Gaaah!”

“Argh!”

The fine horse I was riding didn’t come to a stop until it had trampled the two men blocking the road. The mounted bandits—and even the travelers they had been holding captive—stared at me with their eyes wide.

“You—you bastard!”

I hopped down from the saddle and asked,

“I’m asking just to make sure. You’re the Red Wind Band, right?”

“What the hell are you?”

“Judging by your reaction, I guess I was right. I’m short on time, so let’s finish this quickly.”

Without hesitation, I kicked the leg of the nearest man.

*Crack.*

With a chilling sound, his shinbone snapped, and he collapsed.

It all happened in an instant. The men who had been momentarily stunned quickly thrust curved sabers and spears at me.

“Kill him!”

“A man should always watch his rear.”

“What?”

“Be careful behind you.”

The instant I finished speaking, ten pairs of eyes turned to look behind them.

*Craack! Thud!*

Three fine horses charging at full speed swept the men away.

* * *

The battle was over before it had even begun. The men struck by the horses had been sent flying like bowling pins and lay sprawled out half-dead. The rest were easily subdued.

“P-Please, just spare my life.”

“I won’t kill you. But I’ll have to fix a few things first.”

“Eek!”

While Jin Mukyung methodically broke the limbs of the surviving bandits, Hyuk Mujin brought over the horses tied up beside the road.

“It looks like we can switch to these healthy ones. There must be at least ten of them, so we could take them all and switch whenever they get tired.”

I had been thinking the same thing. Unlike the last group we encountered, these mounted bandits each had their own horses. It was fortunate.

*But still…*

How many of these Red Wind Band bastards were there?

According to the information we obtained at the shrine, more than a hundred remnants had scattered throughout northern Shanxi.

Some were hiding in the foothills, while others were concealed in remote villages or crowded areas, gathering at a designated rendezvous point when ordered.

*These men aren’t stragglers.*

They were ambush forces carrying out an operation. The Red Wind Band Leader was replenishing his forces on the plateau and moving south, while sending the subordinates he had left behind north.

I could easily understand why Wolhwa had described the Red Wind Band Leader as such a terrifying man.

*The judgment to retreat swiftly when the battle turned against him. The meticulousness to prepare his next plan even in the middle of it all. And the drive to carry that plan out.*

On top of that, I had heard that his own martial arts were formidable.

At this point, I almost felt bad for treating him as nothing more than a mounted bandit.

*This has gotten seriously messy.*

Now I understood why the Quest Grade had risen to Peak. And when I thought about it, things seemed to be getting worse by the minute.

It couldn’t be that the Red Wind Band Leader was a Peak master too, could it?

I asked Wolhwa just in case.

She immediately nodded.

“Yes. He is.”

“…Ah.”

“There has to be a reason someone rose to prominence so quickly. He isn’t widely known yet, but according to our sect’s intelligence, the Red Wind Band Leader is indeed a Peak master.”

I was dumbfounded.

“Why would a Peak master become a mounted bandit?”

“There are even Supreme Peak masters among mountain bandits and water bandits. Why couldn’t a mounted bandit be one?”

“Supreme Peak masters? Among mountain bandits and water bandits?”

“When you meet the Green Forest Alliance Leader or the Alliance Leader of the Yangtze River Channel League, ask them yourself. Not that you ever will.”

“…I sincerely hope that’s true.”

A Supreme Peak master? I genuinely hoped I would never meet one.

I shook my head repeatedly and mounted one of the newly taken horses. Jin Mukyung and Hyuk Mujin followed after tying up the Red Wind Band’s mounted bandits and handing them over to the commoners.

> **System**
>
> **Time Limit:** 15:59:13

The time limit continued to tick down even now. Leaving the commoners behind as they bowed deeply in thanks, we kicked the horses in the ribs.

“Giddyap!”

* * *

Deep within the inner grounds of the Mount Heng Sword Sect stood a garden that only a very small number of people were allowed to enter. Cheol Mubaek, the Tiger of Mount Heng, was the only outsider granted that privilege.

“This is my first time here.”

“Because it was a special place. Whenever Father had something weighing on his mind, he would come to the garden.”

Lee Seowol walked through the snow-covered garden, her footsteps crunching softly. Then she suddenly stopped when she spotted a frost-covered flower.

“This was one of Mother’s favorite flowers.”

“Was it?”

“Yes. Whenever she tended the garden, she would always bring me here and tell me the names of the flowers.”

After thinking quietly for a moment, Lee Seowol continued.

“But I can’t remember it now.”

“It was a long time ago. Don’t trouble yourself over it.”

“Uncle Cheol.”

“Yes?”

“I don’t like flowers. I only followed Mother because she liked them. In truth, I never cared about flowers. It’s the same reason Father used to come to the garden.”

Lee Seowol slowly looked around the snow-covered garden. The flowers had withered, and the number of burial mounds in the center of the garden had grown from one to four.

Her gaze sank as she silently stared at the mounds where her family slept.

*Whose fault was it?*

Perhaps it was her own fault for being born the daughter of a Murim martial artist.

That was why she had lost her father and two older brothers one after another, after losing her mother ten years ago.

*I should have kept trying to stop him until the very end…*

A memory from two months ago suddenly resurfaced and blurred her vision.

It had been a conversation between father and daughter, held late one night with no one else present.

*“I’ll have to tie you to the third son of the Jin Family of Taiyuan.”*

*“The third son? Surely you’re not thinking of marrying me to that good-for-nothing?”*

*“No. But it will become an unbearable scandal for you.”*

*“I see.”*

*“Is that all you have to say?”*

*“What can I do? It’s my fault for having a heartless father.”*

*“You’re a child I can never understand. Are you really all right with this?”*

*“If I say I don’t like it, will you change your mind?”*

*“At the very least, I’ll look for another way.”*

*“So the war with the Jin Family of Taiyuan is a foregone conclusion.”*

*“Now that the Strange Hero of Shanxi and the Heaven Shaking Sword are absent, this is the perfect time. This opportunity will never come again.”*

*“The Jin Family of Taiyuan is strong even without the Family Head and the Second Young Master. Please reconsider.”*

*“No. My decision has already been made.”*

*“Then make sure you win. Become strong enough that no one in Shanxi can even open their mouth about a scandal involving me.”*

*“…If you had been a man, I would have made you the Young Sect Leader.”*

*“I’m glad I was born a woman. I have no interest in being this sect’s Young Sect Leader.”*

Her fears soon became reality.

Had even a fortnight passed before Lee Seogeun returned as a cold corpse? Not long after, she lost Lee Cheonbaek, and in the end, even her eldest older brother, Lee Seogwang.

*Now I’m alone.*

And so, the Blood Wolf Sword Lee Cheonbaek’s last surviving blood relative became the new Sect Leader.

A warm palm gently caressed Lee Seowol’s shoulder.

“I’m sorry. I should have come sooner…”

“Uncle Cheol, please don’t say that. If you hadn’t come, our sect wouldn’t have been able to hold out this long.”

Under the Red Wind Band’s fierce assault, the Mount Heng Sword Sect had been helplessly driven back. If not for the Peak master known as the Tiger of Mount Heng, who had rushed over after belatedly learning of Lee Cheonbaek’s calamity, the enemy would never have withdrawn.

“I’ll tear that bastard limb from limb and kill him.”

At the thought of the Red Wind Band Leader, Lee Seowol shook her head.

In a life-and-death duel between Peak masters, Cheol Mubaek had the edge.

They had already clashed once, and Pung Yang had retreated with a minor internal injury.

*But an opportunity like that will never come again.*

The Mount Heng Sword Sect had always gathered information on the mounted bandits of the northern plateau and remained constantly on alert.

There were dozens of mounted-bandit groups on the plateau, but among them, the Red Wind Band led by Pung Yang had grown frighteningly fast.

A man particularly strong and meticulous even among the plateau’s chieftains.

That man was Pung Yang.

*There’s no way someone like that would engage Uncle Cheol in a life-and-death duel. If Uncle Cheol rashly tried to confront him, Pung Yang would turn the tables on him instead.*

Lee Seowol turned toward Cheol Mubaek.

“Uncle Cheol, could you tell me once more about Pung Yang’s martial arts?”

“Early Peak. His saber arts and throwing-knife techniques had reached a high realm. However…”

A deep furrow formed between Cheol Mubaek’s brows.

“Every one of his forms was thoroughly insidious. I suspect he has learned demonic, heterodox martial arts.”

“Demonic, heterodox arts…”

After the Great Faction War, belonging to the evil and heretical paths was tantamount to death in the Central Plains. Unorthodox factions might present themselves as orthodox, but no one openly proclaimed themselves unorthodox.

“For now, it’s only a suspicion. We’ll know if we clash again.”

“I trust you, Uncle Cheol. But don’t underestimate the Red Wind Band Leader. He has any number of subordinates he can sacrifice in his place.”

With enemies bearing down from both directions, their combined force was close to three hundred strong.

Meanwhile, even after gathering every martial artist stationed at its branches, the Mount Heng Sword Sect had less than half that number.

Given the situation, morale was low among both the ordinary martial artists and the newly appointed senior members.

“Seowol. May I say something?”

These were the words of a benefactor who had risked his life out of loyalty to his dead friend. Lee Seowol bowed politely.

“I’ll take your words to heart.”

Cheol Mubaek spoke heavily.

“Leave.”

It was a single word laden with meaning.

But there was not the slightest hesitation in Lee Seowol’s answer.

“I’m sorry.”

“It isn’t too late. You must survive.”

“It isn’t over yet. And I will survive.”

“If you thought Cheonbaek would have wanted this…”

“Uncle.”

At her resolute voice, Cheol Mubaek closed his mouth. Firm determination filled Lee Seowol’s clear eyes.

“This is what I wanted. As the Sect Leader of the Mount Heng Sword Sect.”

“Whew…”

Cheol Mubaek let out a sigh instead of answering.

“I’m already deeply indebted to you, Uncle. Even if you leave now, I won’t resent you.”

“Do you really need to hear my answer before you’ll be satisfied?”

Lee Seowol shook her head. Cheol Mubaek had cherished her like his own child since she was young. In some ways, he had been more of a father to her than her actual father.

“I will never forget this debt. Uncle Cheol, you are the benefactor of both me and the Mount Heng Sword Sect.”

“I’ve watched you since you were little, but… you really are a sly child.”

“I was sly when I was young. Now I’m a ruthless bitch.”

Watching Lee Seowol smile faintly, Cheol Mubaek could only continue to sigh deeply.

“Do we have any chance of winning?”

“If we fought now? Ten percent.”

“What?”

“But if reinforcements arrive, fifty percent. More than that.”

“Reinforcements? From the Jin Family of Taiyuan?”

“A messenger pigeon sent by the Lower District Sect’s Jeongyang Branch arrived four hours ago.”

“How many are there? One hundred? Two hundred?”

“Four. One of them is the Heaven Shaking Sword, Jin Mukyung, and another is…”

Lee Seowol let out a wry laugh, reminded of her ill-fated connection with him.

“The Sleeping Dragon of Shanxi, Jin Taekyung.”
```
