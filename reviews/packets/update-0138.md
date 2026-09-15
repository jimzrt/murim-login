<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0138.txt",
      "sha256": "fe110747544bc49d3ef1ad83cb506ca35493dcda97acd3f8ed8c9b11010c889f",
      "bytes": 13002
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1139b1b04f451b150093aa20914dd794d0be80ce3b6a6918fca11a9f176aa56c",
      "bytes": 2439
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c840818568e54f4f2baf59cce167ea7d2a55f08804ce495893e10072129831a9",
      "bytes": 28334
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "d25e76bf6c8a946edea7ab6011f7a9785511396af15a33ba20198faa2d864ca7",
      "bytes": 755
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b173a9a2617788bf7eb64d5b204b6dfd6fb243fa12158b820616f4d5ad9ec0c9",
      "bytes": 5445
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "7d04c4e2fab5f801eaf701cdf251a1be83c4db882242b7ce85cb3fe8cf21e2d5",
      "bytes": 622
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "2a14a5aa38f8360b1c64433867e8cffe34845633b3995a503177f4c45d8b4409",
      "bytes": 630
    },
    {
      "path": "characters/Woo Jintae.md",
      "sha256": "e69a95d5bd8215ea36a7014df6c7f40b6be503b787fee65f9893cc10b756e325",
      "bytes": 805
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "cbbe10c27be31099e8e07f808e3d10b1c0f3cee7e679577f5241918b482e13ac",
      "bytes": 22950
    }
  ],
  "estimated_tokens": 22232
}
-->

# Durable State Update — Chapter 138

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 138. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 138. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 138,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 138,
    "continuity_sources": [138],
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
    "Woo Jintae is unconscious after Taekyung beats and verbally humiliates him for refusing to apologize.",
    "Taekyung orders the four remaining Five Gates heirs to receive ten sword-case blows each.",
    "The guests at Honghwa Inn recognize Taekyung as the Sleeping Dragon of Shanxi and publicly favor the Jin Family of Taiyuan over the Five Gates of Shanxi.",
    "Jang Childeuk is revealed to be the Level 15 public speaker defending the Jin Family of Taiyuan.",
    "Cheongpung asks to hit the final remaining heir because he has never done so before.",
    "The fall of the Mount Heng Sword Sect has shifted the balance of Shanxi Murim toward the Jin Family of Taiyuan.",
    "The current Five Gates heirs are summoned to Prince Shangshan's luncheon; Woo Jintae remains unconscious and the other four attend while visibly injured.",
    "Seok is the chief steward of Honghwa Inn.",
    "Cheongpung has never experienced a hot spring and joins Taekyung and Mujin after hearing about Honghwa Inn's hot springs.",
    "An unnamed Third-Rank Assistant Military Commissioner has reached eight-tenths mastery of the Seven Plum Sword and is summoned to the luncheon.",
    "Cheongpung's identity remains unknown after he falls asleep following the hot spring.",
    "Hyuk Mujin warns Taekyung about hidden Murim grudges and assassins but bases much of his understanding on wuxia novels.",
    "Prince Shangshan's royal command is delivered to Honghwa Inn by an official accompanied by approximately one hundred soldiers.",
    "Taekyung substitutes Cheongpung as a more impressive young prodigy for the luncheon delegation."
  ],
  "continuity_sources": [
    137
  ],
  "open_questions": [],
  "safe_through": 137,
  "temporary_decisions": [
    "Render 천지신명 as “Heaven and Earth and all the divine spirits.”",
    "Render 엎드려뻗쳐 as lying face down.",
    "Render 첫 경험 빌런 as “first-experience villain.”",
    "Render 칠매검 as “Seven Plum Sword,” 상산왕 as “Prince Shangshan,” and 도지휘첨사 as “Assistant Military Commissioner.”",
    "Render 정 소협 and 갈 소협 as “Young Hero Jeong” and “Young Hero Gal.”",
    "Render 교권 향상 as “Improve teacher authority!”",
    "Render 철전 as “iron coins” and 시진 as “shichen.”",
    "Render 왕명 as “royal command” and 씹덕 as “otaku.”"
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
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 우 소협 | **Young Hero Woo** | Honorific address for Woo Jintae. |
| 황 소저 | **Young Lady Hwang** | Honorific address for an unidentified young woman who is the only daughter of a martial sect. |
| 혁 아우 | **Little Brother Hyuk** | Familiar address for an otherwise unnamed male scion who calls Woo Jintae hyung. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 도동파 | **Dodong Sect** | Fabricated sect claimed by Taekyung when Woo Jintae demands his affiliation. |
| 천진반 | **Tien Shinhan** | Fabricated personal identity claimed by Taekyung. |
| 왕가장 | **Wang Family Estate** | Family estate whose heir is one of the Five Gates scions; he uses sabers rather than sword arts. |
| 왕 공자 | **Young Master Wang** | Heir of the Wang Family Estate. |
| 신 소저 | **Young Lady Shin** | Young woman described as the only daughter of a martial sect. |
| 정 소협 | **Young Hero Jeong** | Address for one injured Five Gates heir; his given name is not stated. |
| 갈 소협 | **Young Hero Gal** | Address for one injured Five Gates heir; his given name is not stated. |
| 석 모 | **Seok** | Self-identification by Honghwa Inn's chief steward; his given name is not stated. |
| 석 총관 | **Chief Steward Seok** | Title and surname form used for Honghwa Inn's chief steward. |
| 칠매검 | **Seven Plum Sword** | Sword art practiced by the unnamed martial official at eight-tenths mastery. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 점소이 검신 되다 | **The Shop Assistant Becomes a Sword God** | Wuxia novel title read by Hyuk Mujin. |
| 아파야 무인이다 | **You Must Hurt to Become a Martial Artist** | Wuxia novel title read by Hyuk Mujin. |
| 무림의 아들 걸어서 구주팔황 세 바퀴 반 | **The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes** | Wuxia novel title read by Hyuk Mujin. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |

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
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 우진태 | 황 소저 | host_to_five_gates_scion | Young Lady Hwang | polite and flirtatious | Woo Jintae presents Shu brocade as a gift while implying personal feelings, then retreats behind a joke. |
| 우진태 | 혁 아우 | older_friendly_sc ion_to_younger_sc ion | Little Brother Hyuk | familiar and patronizing | Woo Jintae promises the male scion an especially impressive gift. |
| 혁 아우 | 우진태 | younger_sc ion_to_older_friendly_sc ion | hyung | familiar and deferential | The scion calls Woo Jintae hyung after they have become close enough to use fraternal terms. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 우진태 | enemy_to_enemy | you / you bastard | insulting-casual | Taekyung repeatedly addresses Woo Jintae with hostile informal forms while demanding an apology and slapping him. |
| 우진태 | 진태경 | enemy_to_enemy | you / little bastard | condescending and enraged | Woo Jintae uses hostile forms such as 네놈, 애새끼, and 어린놈 while trying to intimidate Taekyung. |
| 갈 소협 | 정 소협 | fellow_Five_Gates_heir | Young Hero Jeong | formal-polite | The unnamed heir addresses the other injured heir by surname and honorific. |
| 정 소협 | 갈 소협 | fellow_Five_Gates_heir | Young Hero Gal | formal-polite | The unnamed heir responds using the other injured heir's surname and honorific. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 공일혁    | **Gong Ilhyuk**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 산서오문   | **Five Gates of Shanxi**         |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 137
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Raised by his grandfather in the mountains from age five; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 137
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; traveling as Jin Taekyung’s attendant for the City Lord’s luncheon
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud, hungry for glory, and an avid wuxia-novel reader who sometimes mistakes fictional Murim conventions for reality
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 137
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 137
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family who summons martial officials and young Murim prodigies to a noon luncheon.
- **Personality:** His personal temperament is not established; his authority is treated as commanding and difficult to refuse.
- **Voice:** No direct speech appears in this chapter.
- **Relationships:** Commands the unnamed Third-Rank Assistant Military Commissioner to attend the luncheon and hosts the gathering of young Murim prodigies.

### Woo Jintae.md

# Woo Jintae (우진태)

- **Safe through:** Chapter 137
- **Aliases:** None
- **Role:** Heir of the Seongun Escort Bureau and a leading scion of the current Five Gates of Shanxi; hosts its young members at Honghwa Inn and prepares for the City Lord's luncheon.
- **Personality:** Boastful, calculating, status-conscious, and manipulative; treats lavish gifts and money as tools for creating obligations, but becomes enraged and desperate when publicly humiliated.
- **Voice:** Charming and lavish in public, with polished courtesy that turns dry and contemptuous when he judges someone beneath him.
- **Relationships:** Heir to the Seongun Escort Bureau; cultivates the current Five Gates scions through hospitality, gifts, and bribes.

## Korean source

```text
＃138화



호화로운 육두마차는 거침없이 질주했다.

척 봐도 정예로 보이는 군사들이 앞에서 길을 텄고, 개미처럼 바글바글하던 사람들은 양옆으로 쫙 갈라서서 바람처럼 달려가는 마차를 지켜봤다.

“모세가 이런 기분이었구나.”

내 중얼거림에 청풍이 반응했다.

“모세요? 그게 뭡니까?”

“있어요, 그런 사람이.”

“아, 네.”

혁무진이었다면 또 이상한 소릴 한다며 한참을 투덜거렸겠지만, 청풍은 달랐다.

그는 놀이동산에 온 어린애처럼 신난 얼굴로 마차 이곳저곳을 누르고 두드렸다.

“육두마차는 난생처음 타 봅니다!”

“……사두마차는요?”

“사두마차도 안 타 봤어요!”

“그냥 마차는…….”

“그냥 마차도 타 보고 싶습니다!”

“…….”

지하철이라도 태워 주면 기절하겠는데.

이쯤 되면 안 해 본 걸 세는 것보다 해 본 걸 세는 게 훨씬 빠르겠다.

나는 흥분 상태에 접어든 청풍을 물끄러미 바라봤다.

‘이거 도대체 뭐 하는 놈이야?’

얘를 순수하다고 해야 할지, 멍청하다고 해야 할지.

하긴, 평생을 산에서 살았다고 하니 어쩌면 당연한 것일지도 모른다.

‘다루기가 쉬워서 좋기도 하고.’

방금 그 표정이 잊히지 않는다. 황족이라는 한 단어에 쌍라이트가 번쩍하던 눈동자도.



‘혹시 황족 본 적 있어요?’

‘볼래요! 보겠습니다! 보게 해 주세요!’



그의 눈에 담겼던 건 일반적인 양민들이 가지는 황실에 대한 동경 같은 것이 아니었다. 굳이 따지자면 동물원 코끼리를 보러 가는 설렘이랄까.

‘진짜 특이한 놈일세.’

나만 그렇게 생각하는 건 아닌가 보다.

중상인 우진태를 제외한 산서오문의 후기지수들도 해괴한 것을 보는 듯한 표정으로 청풍을 바라보고 있었다.

“어째 상태가 좀…….”

“정말 이대로 가도 되는 거야?”

“괜히 전하 앞에서 말실수라도 하면 우리까지 피 볼 것 같은데.”

“말실수로 끝나면 다행이지. 황족 처음 봐서 신기하다고 귀라도 잡아당기면 그날로 끝이야, 끝.”

……제법 그럴듯한 추측인데?

후기지수들의 수군거림에 함께 마차에 타고 있던 관리도 불안한 얼굴로 귓속말을 건넸다.

“저기, 진 공자.”

“네?”

“저 사람…… 정말 괜찮은 것 맞소?”

“믿으십쇼. 제가 보증하는 고수라니까요.”

“아니, 고수고 나발이고 정신이 괜찮냐는 말이오.”

“아.”

“차라리 공자와 함께 있던 그 무사를 데려오는 게 더 낫지 않겠소?”

“누구, 아 혁무진이요?”

“그런 이름이었던 것 같소. 내 듣자 하니 그 무사도 상당한 무공의 소유자라던데.”

혁무진이 들었다면 좋아서 펄쩍 뛰었을 얘기다.

문제는 아침에 나한테 맞은 덕분에 얼굴에 시퍼런 멍이 들어 도저히 함께 갈 수 없다는 거지만.

‘그리고 혁무진 정도로는 안 돼.’

어린 왕의 심기를 거스르지 않게 하려면 보다 큰 선물을 가져가야 한다.

나는 걱정하는 관리를 향해 단호하게 고개를 저어 보였다.

“걱정 마십시오. 문제 안 생기도록 제가 책임지고 단속하겠습니다.”

내가 누군가, 명망 높은 태원진가의 직계이자 떠오르는 샛별, 산서 무림의 라이징 스타다.

내 호언장담에 관리의 얼굴이 약간 밝아졌다.

“그럼 본인은 진 공자만 믿겠…….”

우둑.

“……?”

“……?”

잠깐만. 이게 무슨 소리야.

약속이라도 한 듯이 동시에 고개를 돌린 우리의 시선에, 뭔가를 움켜쥐고 있는 청풍이 보였다.

“어, 이게 왜 떨어졌지?”

매우 정교하게 만들어진 황금 용을 들고 헤헤 웃는 녀석의 모습에 한참 침묵하던 관리가 나를 바라봤다.

“진 공자.”

“네.”

“정말 괜찮은 것 맞소?”

나는 고민 끝에 입을 열었다.

“아마도요.”



* * *



저택이 아니라 성(城)이라고 해도 될 만큼 드넓은 공간. 사내의 발걸음은 거침없었다.

굳게 다문 입술과 강건한 눈빛을 마주한 이들은 하나같이 공손히 예를 표했다.

“첨사 어른을 뵙습니다.”

그는 고개를 끄덕이는 것으로 인사를 대신하고 걸음을 재촉했다.

기둥들이 끝없이 늘어선 회랑(回廊)을 지나고 얼마나 걸었을까? 용이 음각된 거대한 철문이 나타나고서야 사내의 발걸음이 멈췄다.

“아뢰게.”

“충.”

그를 향해 군례를 취한 호위군 소속의 장수가 힘차게 외쳤다.

“산서성 도지휘첨사(都指揮僉事), 이풍(李灃) 영감 듭시오!”

얼마 지나지 않아 그에 응답하는 목소리가 들려왔다.

“들라 하라.”

“……!”

어린아이처럼 앳되지도, 그렇다고 장성한 사내처럼 굵지도 않은 목소리.

뭔가를 짐작한 사내, 이풍의 눈썹이 솟구친 그때, 육중한 소리와 함께 철문이 열렸다.

그그긍.

그곳은 호화롭게 치장된 대전(大殿)이었다. 사방이 금은보화로 번쩍거렸고 수십 명이 앉아도 될 만큼 넓은 탁자는 온갖 산해진미로 가득 차 있었다.

다른 사람이라면 입을 딱 벌렸을 만한 광경. 그러나 이풍의 시선은 한곳에 못 박혀 떠날 줄을 몰랐다.

‘저자가 어찌.’

이풍의 시선 끝, 탁자의 상석(上席)에 앉아 있던 한 사람이 빙긋 웃었다.

눈이 부실 만큼 화려한 붉은 비단으로 몸을 휘감은 사내의 입에서 간드러진 목소리가 흘러나왔다.

“이게 누구야, 우리 이 첨사 아니에요?”

우리 이 첨사?

이풍은 지그시 입술을 깨물며 군례를 취했다.

“……도지휘동지(都指揮同知)를 뵙습니다.”

도지휘동지는 종이품으로 각 성에 두 명밖에 없는 고위직.

군 총사령관인 도지휘사와 성주인 상산왕을 제외하면 가장 높은 직책이며, 부사령관인 만큼 실권 또한 막강했다.

실제로 알려진 것은 이러하지만, 눈앞의 사내가 가진 권한은 그 이상이었다.

‘쳐 죽일 놈 같으니.’

간사한 혓바닥과 잔재주로 어린 왕의 눈과 귀를 가리고 제 배만 채우는 간신이자 탐관오리. 그것이 사내에 대한 이풍의 평가였다.

그러나 이풍의 곱지 않은 눈길에도 그의 웃음은 여전했다.

“이 첨사, 오랜만에 보는데 분위기가 너무 험악한 거 아니에요? 혹시 내가 뭐 섭섭하게 한 거라도?”

“……그럴 리가 있습니까. 저는 그저 도지휘동지께서 이런 자리에 계신 것이 뜻밖이라 놀란 것뿐입니다.”

“이런 자리라니?”

“강호의 무부(武夫)들이 모이는 자리입니다. 워낙 거친 자들이라 도지휘동지께서 불편하시지 않을까 염려되는군요.”

말은 위해 주는 것 같지만 속뜻은 다르다. 두 사람 모두 그 사실을 모르지 않았다.

“왜요? 나 이런 자리 좋아해. 그리고 아까부터 호칭이 너무 딱딱하다. 그냥 편하게 불러요. 우리 사이인데 뭐 어때.”

“우리 사이라…… 그게 무슨 사입니까?”

“콩 한 쪽도 나눠 먹는 사이. 전하를 충심으로 보필하는 참된 신하들이지요.”

콩 한 쪽도 나눠 먹어? 참된 신하?

사내의 말에 이풍이 무뚝뚝하게 물었다.

“그럼 편하게 홍 내관이라고 부르면 되겠습니까?”

사내, 홍 내관의 웃음이 순간 경직됐다.

이풍은 고작 한 단어로 그의 역린을 건드렸다.

“그건…… 너무 편한데?”

“저야 말씀을 따른 것뿐입니다.”

“이거 참, 이 첨사가 나를 그 정도로 편하게 생각하는지는 몰랐네.”

“이제라도 제 마음을 알아주시니 몸 둘 바를 모르겠군요.”

“이 첨사.”

“부르셨습니까, 홍 내관. 아니, 다시 도지휘동지라고 불러 드릴까요?”

무겁게 내려앉은 정적.

홍 내관의 입이 다시금 열린 것은 한참 후였다.

“우리 이 첨사, 많이 늘었다?”

“그렇습니까?”

“응, 몇 년 전에 비하면 일취월장했는데?”

“덕분에 여러 가지 배웠습니다.”

“검만 잘 쓰는 줄 알았는데, 오늘 보니 혀도 잘 쓰네. 다시 봤어요.”

“누구보다는 아직 한참 모자랍니다.”

두 사람의 시선이 허공에서 부딪쳤다. 팽팽하게 조여진 공기 속에서 홍 내관이 부드럽게 웃었다.

“뭐, 이 이야기는 나중에 하고…… 내가 뭐 하나만 물어봐도 되려나?”

만만치 않은 상대가 한발 물러났다. 여기서 더 물어뜯었다가는 되레 낭패만 볼 뿐이다. 이풍은 묵묵히 고개를 끄덕였다.

“하문하십시오.”

“이 첨사가 전에 화산파에 있었다고 했죠?”

이풍이 멈칫했다. 그에게 있어 화산파는 그리우면서도 아픈 기억이다.

화산을 떠난 지 이제 어언 십 년이지만 그곳에서의 기억은 여전히 몸과 마음 깊숙이 남아 있었다.

“예. 속가제자였습니다.”

“화산파는 섬서에 있고?”

그와 홍 내관은 이른바 정적(政敵)이라 할 수 있는 관계였다. 그만큼 오히려 속속들이 잘 알았다.

홍 내관은 이런 기본적인 사실을 몰라서 물어볼 만큼 허술하지도, 멍청하지도 않았다.

오히려 속에 구렁이가 백 마리는 득실거리는 교활한 놈이다.

그렇기에 이풍은 더욱 의아함을 느꼈다.

“맞습니다. 그런데 갑자기 그건 왜 물어보시는지?”

“내가 이번에 알게 된 지인이 몇 분 있는데, 혹시 이 첨사도 알까 싶어서.”

“무림인입니까?”

“맞아요. 그것도 섬서 출신.”

“설마 화산……?”

“에이, 그럼 내가 미리 말을 했겠지.”

이풍은 안도의 한숨을 내쉬었다.

결국, 스스로 떠나오긴 했지만 평생을 자랑스러워할 사문(師門)이다. 홍 내관 같은 간신배와 엮이지 않았다는 사실이 천만다행이었다.

“섬서에 문파가 한둘도 아니고, 저도 본산에서 수련하는 중에는 바깥출입을 하지 않았기 때문에 이름을 들어도 잘 모릅니다.”

“그런가? 그럼 얼굴을 보면 알 수도 있겠네?”

“……?”

이풍의 표정을 본 홍 내관이 탁자에 놓인 젓가락을 집어 들었다.

“아까 이 첨사가 물어봤었죠? 내가 왜 이런 자리에 있냐고.”

아름답게 세공된 은 젓가락이 술잔을 두드렸다.

팅. 맑은 소리가 멀리 퍼져 나갔다. 어리둥절한 이풍에게 홍 내관이 눈웃음을 지어 보였다.

“지인을 몇 분 초대했거든. 전하께서 좋아하실 만큼 명성 높고 강한 무인들로.”

동시에 철문 밖에서 힘찬 외침이 들려왔다.

“섬서의 종남삼수(終南三手)가 뵙기를 청합니다!”

“종남삼수…… 종남파!”

이풍의 안색이 급변했다.

화산파와 종남파는 장장 백 년간 섬서의 패권을 다퉈 온 앙숙 관계.

홍 내관의 의도는 지금 짓고 있는 웃음만큼이나 환하기 그지없었다.

“같은 섬서 사람이라 자리를 마련해 봤어요. 괜찮죠?”

이풍이 주먹을 불끈 움켜쥔 그때, 거대한 철문이 열리고 대전 안으로 장대한 체구의 세 사람이 성큼 들어왔다.

그중에 낯익은 얼굴 하나가 끼어 있었다.

“이게 누구야. 화산파의 이풍 아닌가?”

이풍은 몸을 부르르 떨었다. 놈의 얼굴을 본 순간 십 년 전의 그 치욕스러운 기억이 떠올랐기 때문이었다.

“네가 여길 어떻게!”

날카로운 눈매의 사내가 천연덕스럽게 대답했다.

“어떻게 오긴. 산서성의 도지휘동지께서 불러 주시는데 천 리라도 한달음에 달려와야지. 안 그렇습니까?”

“별말씀을. 오히려 초대에 응해 주셔서 감사할 따름이에요.”

으드득, 이를 가는 이풍을 향해 종남삼수의 셋째, 공일혁이 씩 웃어 보였다.

“그나저나 출세했네. 자네 주제에 도지휘첨사라…… 화산에서 은자깨나 뿌렸겠어. 응?”

“네놈이 감히 화산파를 모욕해?”

“응? 화산파를 모욕한 건 자네지. 십 년 전, 그 대단한 화산 무공으로 백여 초 만에 무릎을 꿇은 게 누구였나?”

“이놈-!”

이풍의 입에서 벼락같은 외침이 터져 나왔다.

그가 화염이 줄기줄기 쏟아지는 눈동자로 공일혁을 노려보던 그 순간. 철문 밖에서 세 번째 외침이 들려왔다.

“산서 무림의 후기지수들이 뵙기를 청합니다!”
```

## Final English reading copy

```markdown
# Chapter 138

The luxurious six-horse carriage raced onward without slowing.

Soldiers who looked like elite troops cleared the road ahead, while the people who had been swarming around like ants split neatly to either side and watched the carriage dash past like the wind.

“So this is how Moses felt.”

Cheongpung reacted to my mutter.

“Moses? Who is that?”

“Someone.”

“Oh, I see.”

If it had been Hyuk Mujin, he would have complained for ages about me saying something strange, but Cheongpung was different.

He had the excited expression of a child at an amusement park as he pressed and tapped every part of the carriage.

“This is my first time riding in a six-horse carriage!”

“…What about a four-horse carriage?”

“I’ve never ridden in one of those, either!”

“What about an ordinary carriage…?”

“I’d like to ride in one of those, too!”

“…”

If I put him on a subway, he would probably faint.

At this point, it would be much faster to count the things he had done than the things he had never done.

I stared at Cheongpung, who had entered a state of total excitement.

*What the hell is this guy?*

Was he innocent or stupid?

Then again, he had said he had lived his entire life in the mountains. Maybe this was only natural.

*At least he’s easy to handle.*

I still couldn’t forget the expression he had just made. His eyes had lit up like high beams at the mere mention of the imperial family.

*“Have you ever seen a member of the imperial family?”*

*“I want to! I’ll see one! Please let me see one!”*

What filled his eyes wasn’t the sort of admiration ordinary commoners felt toward the imperial family. If I had to compare it to something, it was more like the excitement of going to see an elephant at the zoo.

*He really is a strange one.*

Apparently, I wasn’t the only one who thought so.

The young prodigies of the Five Gates of Shanxi, excluding the severely injured Woo Jintae, were staring at Cheongpung as if they were looking at something bizarre.

“Is he really all right…?”

“Can we really go like this?”

“If he says something inappropriate in front of His Highness, we might get dragged into it, too.”

“It’ll be lucky if it ends with him saying something inappropriate. If he gets excited about seeing an imperial family member for the first time and pulls on his ear, we’re finished. Completely finished.”

…That was a surprisingly plausible prediction.

Hearing the young prodigies whispering, the official riding in the carriage with us leaned over and spoke in an anxious voice.

“Um, Young Master Jin.”

“Yes?”

“That person… Is he really all right?”

“Believe me. He’s a master I can vouch for.”

“To hell with whether he’s a master. I’m asking whether he’s right in the head.”

“Oh.”

“Wouldn’t it be better to bring along the martial artist who was with you instead?”

“Who? Ah, Hyuk Mujin?”

“I believe that was his name. I hear he’s also quite skilled in martial arts.”

If Mujin had heard that, he would have jumped for joy.

The problem was that he had a dark blue bruise on his face from getting beaten by me that morning, so there was no way he could come along.

*And Hyuk Mujin wouldn’t be enough.*

To avoid offending the young prince, I needed to bring a more impressive gift.

I firmly shook my head at the worried official.

“Don’t worry. I’ll take responsibility for making sure nothing happens.”

Who was I? A direct descendant of the prestigious Jin Family of Taiyuan, a rising star, and Shanxi Murim’s newest sensation.

My bold assurance brightened the official’s expression a little.

“Then I’ll trust Young Master Jin—”

*Crack.*

“…?”

“…?”

Wait a second. What was that sound?

As though we had made a pact, we all turned our heads at the same time.

There was Cheongpung, clutching something in his hands.

“Huh? Why did this fall off?”

The official stared at me in silence for a long moment as Cheongpung grinned foolishly while holding an exquisitely crafted golden dragon.

“Young Master Jin.”

“Yes?”

“Is he really all right?”

After thinking it over, I opened my mouth.

“Probably.”

* * *

The space was so vast that it could have been called a castle rather than a residence. A man strode through it without hesitation.

Everyone who saw his tightly pressed lips and resolute gaze respectfully paid their respects.

“Greetings, Assistant Military Commissioner.”

He acknowledged them with a nod and quickened his pace.

After passing through a corridor lined with endless pillars, how long had he been walking? The man finally stopped when a massive iron gate engraved with a dragon appeared before him.

“Announce me.”

“Yes, sir.”

A commander from the palace guard saluted him and called out in a powerful voice.

“His Excellency Li Feng, Assistant Military Commissioner of Shanxi Province, entering!”

Before long, a voice answered from within.

“Let him enter.”

“…”

The voice was neither as high and childish as a little boy’s nor as deep as a grown man’s.

At the moment the man—Li Feng—seemed to realize something and his eyebrows shot up, the iron gate opened with a heavy groan.

*Grrrnnng.*

Beyond it was an extravagantly decorated grand hall. Gold and silver treasures glittered in every direction, and a table large enough for dozens of people was covered with every delicacy from land and sea.

It was a sight that would have left anyone else gaping. But Li Feng’s gaze remained fixed on a single point.

*How is he here?*

At the end of Li Feng’s gaze, a man seated at the head of the table smiled faintly.

Wrapped in dazzling red silk, the man spoke in a coy, lilting voice.

“Well, well. If it isn’t our Assistant Commissioner Li.”

*Our Assistant Commissioner Li?*

Li Feng bit down on his lips and performed a military salute.

“…Greetings, Deputy Military Commissioner.”

The Deputy Military Commissioner was a second-rank official, with only two such posts in each province.

Aside from the Military Commissioner, who was the commander-in-chief, and the City Lord, Prince Shangshan, it was the highest position there was. As the deputy commander, he also wielded tremendous authority.

That was what people knew publicly. In truth, the man before him possessed even greater power.

*That bastard deserves to be beaten to death.*

A sycophant and corrupt official who used his glib tongue and petty tricks to blind the young prince’s eyes and ears while lining his own pockets. That was Li Feng’s assessment of him.

But even beneath Li Feng’s openly hostile gaze, the man continued smiling.

“Assistant Commissioner Li, it’s been a while. Isn’t the atmosphere a little too tense? Did I perhaps do something to offend you?”

“…Of course not. I was merely surprised to find you in a place like this, Deputy Military Commissioner.”

“A place like this?”

“It is a gathering of martial artists from the martial world. They are rather rough people, so I was concerned that you might be uncomfortable, Deputy Military Commissioner.”

His words sounded considerate, but their true meaning was different. Neither man was unaware of that.

“What’s the problem? I like places like this. Besides, you’ve been so stiff with your title since a while ago. Just call me whatever you like. We’re close enough, aren’t we?”

“Close enough for what, exactly?”

“We’re the kind of people who would split a bean between us. True loyal subjects who serve His Highness with all our hearts.”

*Split a bean between us? True loyal subjects?*

Li Feng asked bluntly,

“Then may I call you Eunuch Hong?”

The smile on Eunuch Hong’s face stiffened for a moment.

With a single word, Li Feng had touched his sore spot.

“That’s… a little too familiar, don’t you think?”

“I only followed your instructions.”

“Well, this is something. I didn’t realize Assistant Commissioner Li considered me that close.”

“I’m overwhelmed that you understand my feelings at last.”

“Assistant Commissioner Li.”

“Did you call, Eunuch Hong? Or should I go back to calling you Deputy Military Commissioner?”

A heavy silence settled over the hall.

It was a long while before Eunuch Hong opened his mouth again.

“Our Assistant Commissioner Li has improved quite a bit, hasn’t he?”

“Have I?”

“Yes. Compared to a few years ago, you’ve made remarkable progress.”

“I’ve learned many things thanks to you.”

“I thought you were only good with a sword, but now I see you’re good with your tongue, too. I’ll have to look at you differently.”

“I’m still nowhere near as skilled as someone else.”

Their gazes collided in midair. Within the tightly stretched silence, Eunuch Hong smiled gently.

“Well, we can talk about that later… May I ask you one thing?”

His opponent was no pushover, but he had taken a step back. If he kept biting at him, he would only end up at a disadvantage. Li Feng silently nodded.

“Ask.”

“You said you used to belong to Huashan, didn’t you?”

Li Feng paused. Huashan was a place he both missed and remembered with pain.

It had been nearly ten years since he had left Mount Hua, but the memories of that time still remained deep in his body and heart.

“Yes. I was a lay disciple.”

“And Huashan is in Shaanxi?”

He and Eunuch Hong were what one might call political enemies. For that very reason, they knew one another inside and out.

Eunuch Hong was neither careless nor stupid enough to ask about such a basic fact without a reason.

If anything, he was a crafty man with a hundred snakes writhing inside him.

That was why Li Feng was even more puzzled.

“That’s right. But why are you suddenly asking?”

“I’ve come to know a few people recently, and I wondered if you might know them, too.”

“Are they martial artists?”

“Yes. And they’re from Shaanxi.”

“Don’t tell me they’re from Huashan…?”

“Oh, come on. If they were, I would have told you already.”

Li Feng let out a sigh of relief.

In the end, he had left of his own accord, but Huashan was still the sect he would be proud of for the rest of his life. It was a tremendous relief that he had not been entangled with a sycophant like Eunuch Hong.

“There are more than one or two sects in Shaanxi. And I didn’t go outside while training at the main sect, so even if I heard their names, I might not recognize them.”

“Is that so? Then perhaps you would recognize them if you saw their faces?”

“…?”

Seeing Li Feng’s expression, Eunuch Hong picked up the chopsticks lying on the table.

“You asked earlier why I was here, didn’t you?”

The beautifully crafted silver chopsticks tapped against a wine cup.

*Ping.*

The clear sound spread through the hall.

Eunuch Hong gave the bewildered Li Feng a knowing smile.

“I invited a few acquaintances. Famous and powerful martial artists whom His Highness would enjoy meeting.”

At that moment, a powerful shout rang out from beyond the iron gate.

“The Three Hands of Zhongnan request an audience!”

“The Three Hands of Zhongnan… The Zhongnan Sect!”

Li Feng’s complexion changed drastically.

Huashan and the Zhongnan Sect had been bitter rivals fighting for supremacy in Shaanxi for a full hundred years.

Eunuch Hong’s intentions were every bit as clear as the smile on his face.

“They’re from Shaanxi, so I thought I’d arrange a gathering. Isn’t that nice?”

Just as Li Feng clenched his fists, the massive iron gate opened and three imposing men strode into the hall.

One of them had a familiar face.

“Well, well. If it isn’t Li Feng of Huashan?”

Li Feng’s body trembled. The moment he saw that man’s face, the humiliating memory from ten years ago came rushing back.

“How did you get here?”

The sharp-eyed man answered casually.

“How did I get here? When the Deputy Military Commissioner of Shanxi Province invites you, you have to come running even if it’s a thousand li away. Isn’t that right?”

“There’s no need to thank me. I’m the one grateful that you accepted the invitation.”

*Grind.*

Gong Ilhyuk, the third of the Three Hands of Zhongnan, grinned at Li Feng as he ground his teeth.

“Anyway, you’ve done well for yourself. Assistant Military Commissioner, someone like you… Huashan must have spread around quite a bit of silver for you. Hmm?”

“How dare you insult Huashan?”

“Insult Huashan? You’re the one who insulted it. Ten years ago, who was it that knelt after a little over a hundred exchanges against that magnificent Huashan martial arts?”

“You bastard!”

A thunderous shout burst from Li Feng’s mouth.

At the moment he glared at Gong Ilhyuk with eyes that seemed to pour out streams of flame, a third shout rang out from beyond the iron gate.

“The young prodigies of Shanxi Murim request an audience!”
```
