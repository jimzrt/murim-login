<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0126.txt",
      "sha256": "6ae42d26cc8e2dcb04cac31ec7767f9a9edc6d991f22187fa2c9a843964444af",
      "bytes": 14969
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "623a170f58898c7a503dce43b67359210f032817b21cf3f1c64aa4f352ed361c",
      "bytes": 4942
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f26c08cba63fee9d0f88d924236e2b9e802757717ff6d1cc28e0f4039f074291",
      "bytes": 21109
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "a2a5c6cb035c217958b294a5082cca5e93ac7fc8c4d9077630e7291bafd6bd1b",
      "bytes": 5199
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "1f8a0225f95c92db88fa6697fefa42ac53a0851992bbfd90ccb1774e54e014aa",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7dcd432c0c535a701ee7423607b389eb4a467e9201dcefe26c2ad9915a03f10a",
      "bytes": 24327
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "5001660a7a4809907d0ff8544548b838177832e4bdc15a7ee5c565529983c01f",
      "bytes": 8154
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "ffcab13cfabaad08943000d9421df0669328da02f195819a1b240850589489ec",
      "bytes": 1356
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "5d0d5e3a694926928aed675282dab5191ab53a151bc7966f2ad03776c377d282",
      "bytes": 4604
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3db4c10def570c6e7f1232dd9e16bc8bda6266e46a77c75c477139a09f35c0f6",
      "bytes": 18614
    }
  ],
  "estimated_tokens": 21715
}
-->

# Durable State Update — Chapter 126

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 126. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 126. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 126,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 126,
    "continuity_sources": [126],
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
    "Jin Mukyung survived his fight with Pung Yang and returned to the Jin Family of Taiyuan, but remains incompletely recovered after only four days of healing.",
    "Cheol Mubaek remains severely injured and needs extended recuperation; he is the ninth-generation successor of the Shura Annihilating Fist and protector of Lee Seowol.",
    "Lee Seowol remains the seventeen-year-old Sect Leader of the Mount Heng Sword Sect and vows to preserve it for those who died defending it.",
    "The Lower District Sect sent a relief force with physicians, cooks, and laborers after the battle.",
    "Wolhwa's real name is Eun Sowol, and she is the Lower District Sect's Shanxi Branch Leader with authority over more than thirty Shanxi branches.",
    "Lee Seowol accepted Jin Wikyung's invitation to the Jin Family of Taiyuan's New Year gathering and offered the Mount Heng Sword Sect's territorial rights to the Jin Family as an apology.",
    "Lee Seowol proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist; Taekyung has decided to reject the proposal because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty with its available medicine.",
    "The Lower District Sect is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued the Mount Heng Sword Sect.",
    "Cheol Mubaek and Lee Cheonbaek first met more than thirty years ago, fought, and became close friends; the Shura Annihilating Fist was an ancient top-ten fist technique whose lineage was believed to have ended and is no longer current among the top ten.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm; Taekyung possesses its manual, a Fire Gate Clan secret restricted to owners of Scorching Yang Qi.",
    "The Fire King is a Supreme Peak master among the world's twenty greatest experts; his current status is unknown, and the Fire Gate Clan has a single successor.",
    "The Mount Heng Sword Sect formally apologized for Lee Cheonbaek's crimes, but Taekyung refused the apology and directed responsibility toward the Jin Family of Taiyuan.",
    "The Temporary Strength Pill has an unknown maker and unknown Grade, temporarily raises latent power, grants +100 combat stats and fifteen years of internal energy, enables Body-Protecting Qi, and has an unspecified price or aftereffect."
  ],
  "continuity_sources": [
    125
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What is the Temporary Strength Pill's origin, exact price, and long-term aftereffect?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "Was Jopil truly the nineteenth-generation successor of the Flame Divine Palm, and how did he acquire it?",
    "Who called out to Jin Mukyung and Jin Taekyung from the distance at the chapter's end?"
  ],
  "safe_through": 125,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 호신강기 as Body-Protecting Qi.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, and 시진 as shichen.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, and 천하십대권법 as the ten greatest fist techniques in the world.",
    "Render 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, and 아이템창 as Item Window; retain the Samsung/Samseong clarification footnote."
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

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 삭주 | **Sakju** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 평화 | **Peace Guild** | Guild name. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 125
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; stationed outside Jin Taekyung’s pavilion while Taekyung recovers
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 125
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 122
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 125
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 125
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 105
- **Aliases:** Ghost Sword
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung

## Korean source

```text
＃126화



나흘 전, 모든 임무를 끝마치고 태원진가로 복귀한 위팽은 자신의 빠른 일 처리를 뼛속 깊이 후회했다.

‘하루만 늦게 올걸.’

그러나 이미 늦었다. 하오문의 전서응을 받은 진위경이 눈을 까뒤집고 길길이 날뛰고 있었으니까.

“이 개 같은 마적 놈들이 감히!”

“또 무슨 일입니까?”

“풍양, 적풍단, 항산검문, 내 동생들, 위험! 매우 위험! 당장 출발!”

“……호위대 소집하겠습니다.”

모든 장애물을 치워 버린 지금, 진위경의 권위는 절대적이었다. 반 시진이 채 지나기도 전에 두 사람은 오십 명의 정예 호위대와 함께 가문을 나섰고, 쉬지 않고 내달렸다.

그리고 이틀 후, 말을 갈아타기 위해 들른 하오문 지부에서 새로운 소식을 접했다.

“뭐라? 풍양이 죽고 적풍단이 궤멸했어?”

“옛! 본 문이 파악한 바에 의하면, 삼백여 명에 달하는 적의 병력 대부분이 몰살당했고 진태경 공자께서 풍양을 쓰러트리셨답니다.”

“오오, 오오오. 태경이가!”

세상을 다 가진 듯한 진위경의 웃음은 이어지는 말에 씻은 듯이 사라졌다.

“다시 한번 말해 보게. 무경이가 어찌 되었다고?”

“그, 그게, 풍양과의 생사결에서 상당한 부상을 입으셨다고…… 하지만 목숨에도 지장 없고 빠르게 회복 중이니 걱정하실 필요 없을 듯싶습니다.”

이미 틀렸다. 진위경의 귀에는 ‘상당한 부상’밖에 들리지 않았을 것이다.

어릴 적 아우들의 손가락에 가시라도 박히는 날이면 마치 손가락이 잘린 것처럼 야단법석을 피워 대던 그다.

‘그런데 약간의 부상도 아니고 상당한 부상이라니. 난리 났군.’

위팽은 지금까지의 경험을 토대로 다음 순간 벌어질 상황을 예측했고, 아니나 다를까 정확히 들어맞았다.

“무경이가 사경을 헤맨다니!”

진위경의 포효에 하오문도가 눈을 깜빡였다.

“예, 예?”

“풍양! 네놈이 감히 내 아우를 죽여!”

상당한 부상에서 사경을 헤매게 하더니, 이제는 죽이기까지 한다. 뒤늦게 정신을 차린 하오문도가 황급히 입을 열었다.

“저기, 소가주님. 뭔가 엄청난 오해가 있는 모양이신데…….”

“내 반드시 네놈의 사지를 갈기갈기 찢어 구주에 뿌리리라!”

“…….”

“…….”

진위경의 분노는 다시 하루가 지난 다음에야 누그러졌다.

“무경이와 태경이가 어제 항산검문에서 출발했다고?”

“예. 그러니까 이제 적당히 좀 하십쇼.”

“둘 다 무사한 건가?”

“안 무사했으면 수레에 실려서 오지, 마차 타고 오겠습니까?”

“그럼…….”

“내일 정오 무렵에는 만나실 수 있을 겁니다.”

비로소 쉴 수 있다고 생각하니 위팽은 속이 다 후련했다.

자신이 누군가, 귀검(鬼劍)이라는 별호까지 붙은 절정 고수다. 당장 어디를 가도 한 자리 차지할 수 있는 실력자인데 주군을 잘못 섬기는 바람에 이런 극한의 노동에 시달리고 있었다.

‘마지막으로 술을 마신 게 언제더라.’

오늘은 드디어 오리 구이에 따끈한 술 한잔 걸칠 수 있겠다. 위팽의 입가에 흐뭇한 미소가 맺힌 그 순간이었다.

“좋아. 그럼 빨리 준비하자고.”

“예? 뭘 준비합니까?”

“내 아우들이 수많은 역경을 딛고 임무를 성공적으로 마쳤으니 환영식을 열어야지.”

“……저는 뭐, 보름이 넘도록 강호 유람하다가 온 겁니까?”

“응? 누구? 아, 자네?”

눈을 깜빡이며 위팽을 바라보던 진위경이 호탕하게 웃었다.

“그거야 물론 자네도 포함이지! 설마 내가 잊고 있었겠나?”

이 인간, 설마 했는데 잊고 있었던 게 분명하다.

황당한 얼굴로 입만 벙긋거리는 위팽에게 진위경이 말했다.

“아, 수하들 시켜서 인근 포목점에서 천 좀 사 오게나. 최대한 큼지막한 것으로.”

“천을요? 갑자기 그건 또 왜요?”

“생각해 놓은 게 있네.”



* * *



“……그렇게 된 겁니다.”

못 본 사이 10년은 늙어 버린 위팽의 말을 들으며 주위를 둘러봤다.

항산검문을 출발한 지 이틀 만에 도착한 삭주(朔州)에는 때아닌 인파가 바글거렸고, 입구에는 검은 글씨가 적힌 거대한 흰색 천이 나부꼈다.



진무경, 진태경, 그리고 혁무진의 무사귀환을 축하합니다!

- 태원진가 일동 -



나도 모르게 신음이 흘러나왔다.

“오메 시벌, 저게 뭐여…….”

살다 살다 저런 건 처음 본다.

가로 길이만 20여 장에 달하는 같은 현수막. 넓은 대로(大路)를 사이에 두고 마주 보는 두 전각의 꼭대기에 연결된 그것은 항산검문에서도 보일 것 같았다.

‘쓸데없이 글씨체 용사비등한 것 보소.’

자식 명문대 보낸 극성 부모도 이 정도는 아니겠다.

나와 진무경, 혁무진은 약속이라도 한 듯 입을 벌리고 현수막을 바라봤다.

“제 이름은 왜 작죠?”

무슨 소린가 해서 다시 보니 아주 작은 글씨로 혁무진의 이름까지 들어가 있다.

“글씨 크기 작아서 섭섭하냐? 난 기쁠 것 같은데.”

“이상하잖아요. 아래에서 보면 잘 보이지도 않아요.”

“그럼 내 이름 빼고 네 거 넣을래? 진심이야.”

잠시 고민하던 혁무진이 대답했다.

“생각해 보니까 지금도 괜찮은 것 같습니다.”

“그럼 입 닥치고 있어.”

“옙.”

대화는 더 이상 이어지지 못했다. 극성 부모, 아니 진위경이 세상에서 가장 환한 웃음을 지으며 달려왔기 때문이다.

“이 녀석들!”

이게 사람이냐 불곰이냐.

2m가 넘어 가는 거한이 솥뚜껑만 한 손으로 나와 진무경을 끌어당겼다. 이대로 으스러져도 이상하지 않을 만큼 우악스러운 힘이다.

“무사해서 다행이다. 정말 다행이야!”

무사했다. 진위경이 있는 힘껏 끌어안기 전까지는.

우두둑.

“커헉!”

“헉, 무경아!”

……지금은 별로 무사하지 않은 것 같군.

고통에 몸을 부르르 떠는 피해자를 끌어안은 가해자가 소리쳤다.

“의원! 의원!”

“의원 불러야 할 것 같은데요? 진짜 아파 보이는데.”

내 질문에 위팽이 피곤한 얼굴로 대답했다.

“하루 이틀입니까? 이럴 줄 알고 미리 불러 놨습니다.”

“오오오.”

처음으로 위팽이 위대하게 느껴지는 순간이었다.



* * *



나를 포함한 태원진가의 삼 형제와 위팽이 한자리에 모인 것은 해가 떨어진 직후였다.

진무경이 한층 두꺼워진 붕대 차림으로 나타나자 진위경이 눈치를 살폈다.

“괜찮으냐?”

“주군 같으면 괜찮으시겠습니까? 가뜩이나 다친 사람을 그렇게 막 다루시면 어떡합니까?”

“나름 살살 한 건데…….”

무공으로는 모르겠지만 신체 피지컬로 따지자면 진위경이 산서제일인이다.

나는 슬그머니 의자를 옆으로 밀었고, 진무경은 초췌한 얼굴로 대답했다.

“전 괜찮습니다.”

“…….”

전혀 안 괜찮아 보이는데.

진무경이 절정 고수라 다행이지, 무공 한 수 익히지 못한 양민이었다면 걸어 다니지도 못했다.

“이공자께서 부상을 입었다고 듣긴 했습니다만, 이 정도일 줄은 몰랐군요. 아직 내상도 다 낫지 않았던데…….”

“정말 그 풍양이란 놈이 한 짓이냐?”

두 사람의 물음에 진무경이 담담하게 수긍했다.

“강하더군요. 생각 이상으로.”

진무경이 누군가. 천하에서도 주목하는 촉망받는 후기지수다. 눈부신 천재성과 노력을 바탕으로 일찍이 절정의 경지에 오른 그가 일개 마적 우두머리에게 패배한 것이다.

“놈이 그 정도의 강자라는 말씀이십니까?”

“풍양이라, 고원의 마적 중에 제법 뛰어난 고수들이 있다고는 들었지만. 글쎄…….”

문득 두 사람의 시선이 나를 향했다. 오리 구이는 그만 처먹고 말 좀 해 보라는 무언의 압박.

입 안 가득 쑤셔 넣은 음식을 꿀꺽 삼키고 입을 열었다.

“사실이에요. 항산호 대협 소식은 들어서 아시죠? 그 양반도 팔다리 아작 나서 요즘 휠체어 타고 다닙니다.”

“휭최어가 뭡니까?”

“아, 수레요, 수레.”

진위경이 굵은 손가락으로 탁자를 두드렸다.

“그 정도의 고수라면 진작 알려졌을 텐데. 혹 무경이 네가 방심한 것은 아니냐?”

이번엔 진무경이 망설임 없이 고개를 저었다.

“미처 예상치 못한 수에 당하긴 했지만 그게 변명이 될 수는 없습니다. 다시 싸운다 해도 결과는 같을 겁니다.”

“……그 정도였더냐?”

“호신강기(護身罡氣)를 사용하더군요. 압도적이었습니다.”

진위경과 위팽이 동시에 눈을 부릅떴다.

“호신강기!”

“이공자, 그게 사실입니까?”

굳이 대답은 필요 없었다. 진무경이 그런 뻔한 거짓말을 할 이유가 없으니까. 경악한 두 사람을 향해 진무경이 다시 말을 이었다.

“지금까지 싸워 본 적 중 가장 강했습니다. 아니, 정확히는 강해졌다고 해야 맞을 것 같습니다.”

“강해졌다니?”

“그건 또 무슨…….”

“피처럼 붉은 단환 한 알을 삼키자마자 무섭도록 강해지더군요.”

드디어 잠력단에 관한 이야기가 나온다.

나는 최대한 자연스럽게 행동하려 애썼다.

‘내가 갖고 있다는 사실을 들키면 안 돼.’

잠력단은 독이 든 성배다. 분명 불길하고 수상쩍은 물건이지만 엄청난 효력을 지니고 있음을 부정할 수는 없다.

나는 이미 죽음이라는 최악(最惡)의 순간에 쓸 수 있는 차악(次惡)의 대비책으로 잠력단을 사용하기로 마음먹었다.

“짧은 순간이었지만 놈이 단환을 복용하려 할 때 분명 목갑 안에 한 알이 남아 있는 걸 봤는데…….”

진무경이 말꼬리를 흐리며 나를 바라본다.

“혹시 나중에라도 풍양의 품에서 뭔가 발견하지 못했느냐?”

“응? 뭐가.”

“목갑이라든지. 내가 말한 붉은 단환이라든지.”

나는 짐짓 눈살을 찌푸렸다.

“잘 모르겠는데? 나중에 뭐 있나 싶어서 뒤져 봤는데 웬 나무 쪼가리만 우수수 쏟아지더라니, 그게 목갑 파편이었나?”

“그럼 단환, 단환은?”

“모르지. 당장 나도 힘들어서 죽겠는데 어떻게 그걸 다 뒤져 보겠어.”

이 정도면 제법 그럴싸한 핑계다.

사람이 한두 명 죽은 것도 아니고, 워낙 격렬한 전투였으니 지쳐서 못 찾아본 것도 어쩜 당연한 일인데 더 무슨 말을 하겠나.

“그런가?”

“항산검문 사람들이 발견했을 수도 있고, 아니면 널리고 널린 피 웅덩이에 그대로 녹아 버렸을 수도 있겠지.”

“흠.”

진무경이 약간 의구심 어린 눈빛으로 나를 응시했지만 그냥 어깨만 으쓱해 보였다.

‘어차피 뒤져 봐도 안 나온다. 이놈아.’

나만이 열고 닫을 수 있는 최고의 금고, 인벤토리 한구석에 고이 모셔 뒀으니 진무경이 아니라 천하의 어떤 대도(大盜)라고 해도 잠력단의 털끝 하나 건드릴 수 없다.

‘참 편하단 말이지.’

내가 다시 한번 시스템의 편리함에 감탄하고 있을 때, 진위경과 위팽은 잠력단의 정체에 대해 유추하기 시작했다.

“볼 것도 없이 사마외도의 유산이겠군. 정마대전 당시에 비슷한 효력의 단환이 상당수 사용되었다고 들은 기억이 있다.”

“한때 고원을 비롯한 산서 북부가 마교(魔敎)의 손아귀에 떨어진 적이 있었지요. 풍양이 그 흔적을 발견한 거라면 얼추 맞아떨어집니다.”

귀를 쫑긋 세우고 듣다가 멈칫했다.

‘잠깐만. 마교?’

마교란 무협 소설에서 절대 빠지지 않는 단골손님이자 약방의 감초, 금잔디의 명예 소방관 같은 존재다.

물론 세계 평화와 빈민 구제를 위해 힘쓰는 종교 단체는 아니고, 일종의 IS(이슬람 테러 단체)라고 할 수 있겠다.

한 줄 요약하자면, 엮여서 좋은 점이 단 하나도 없는 광신도 집단이라는 거지.

‘마교에서 잠력단을 만들었다면?’

지옥에서 막 올라온 악마처럼 붉게 물들었던 풍양의 눈동자. 상상을 뛰어넘는 힘을 일시적으로나마 선사하던 비상식적인 효능.

‘이거, 그림이 대충 그려지는데.’

찝찝하다. 더럽게 찝찝하다!

하지만 고통 없이 얻어지는 것은 없는 법. 부작용도 충분히 감당할 만한…….

“그때 당시에 마교도들이 사용했던 대표적인 것이 폭혈단(爆血團)이었지, 아마.”

“말로만 들어 봤습니다. 두 시진만 지나면 전신의 혈맥이 터져서 죽는다면서요?”

“사술(詐術)로 힘을 얻으려 한 대가지.”

“폭혈단이 그 정도인데 풍양이란 놈이 쓴 건 도대체 어느 정도일까요?”

“글쎄, 모르긴 몰라도 부작용이 상상을 초월하겠지. 선천지기가 상하는 것은 물론이고 제한 시간이 끝나면 몸에 큰 무리가 갈 걸세. 결국, 제 몸을 장작 삼아 짧은 시간을 불태우는 역할이니까.”

절로 마른침이 넘어간다. 나도 모르게 목소리가 튀어나왔다.

“그다음은요?”

“마교에서 만든 물건이니 오죽하겠느냐. 마기(魔氣)가 골수까지 치밀면…… 피밖에 모르는 살인귀가 되겠지.”

“……살인귀요? 마기가 골수까지 치밀어요?”

“그런 물건이 악인의 손에 들어가면 실로 큰일…… 태경아, 왜 그러느냐?”

진위경이 걱정스러운 얼굴로 나를 바라본다. 슬쩍 이마를 문질러 보니 땀이 송골송골 맺혀 있었다.

“그냥요, 좀 더워서.”

진무경이 퉁명스럽게 대꾸했다.

“무슨 소리야. 밖에 눈 오는데.”

“소음인 주제에 뭘 알아. 난 태양인이라 그래…….”

젠장. 이제 내가 무슨 말을 하는지도 모르겠다.

나는 세 사람을 향해 어색하게 웃어 보였다.

“저기. 아까 깜빡한 게 있는데요.”

“……?”

“……?”

“……?”

“그 환단. 생각해 보니까 제가 갖고 있네요. 허허, 허허허.”

“……!”

“……!”

“……!”
```

## Final English reading copy

```markdown
# Chapter 126

Four days ago, after completing every mission and returning to the Jin Family of Taiyuan, Wipeng deeply regretted how efficiently he had handled things.

*I should have come back a day later.*

But it was already too late. Jin Wikyung had received a messenger eagle from the Lower District Sect and was raging with his eyes bulging out of his head.

“Those goddamned mounted bandits dare!”

“What happened now?”

“Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, my brothers—they’re in danger! Great danger! We leave at once!”

“...I’ll assemble the guards.”

Now that every obstacle had been removed, Jin Wikyung’s authority was absolute. Before even half a shichen had passed, the two of them left the family with fifty elite guards and raced off without stopping.

Two days later, while changing horses at a Lower District Sect branch, they received new information.

“What? Pung Yang is dead, and the Red Wind Band has been annihilated?”

“Yes! According to what our sect has learned, most of the enemy forces, numbering around three hundred, were slaughtered. Young Master Jin Taekyung defeated Pung Yang himself.”

“Oh. Ohhh. Taekyung!”

Jin Wikyung’s laughter, as if he had gained the whole world, vanished at the next words.

“Tell me again. What happened to Mukyung?”

“Th-that is... He suffered a considerable injury in his life-and-death duel with Pung Yang... But his life is not in danger, and he is recovering quickly, so you likely have nothing to worry about.”

It was already over. Jin Wikyung had probably heard nothing except *considerable injury*.

When his younger brothers were children, if even a thorn pierced one of their fingers, he would raise such a commotion that you would have thought the finger had been severed.

*And it wasn’t a minor injury. It was a considerable one. This is going to be a disaster.*

Based on his experience so far, Wipeng predicted what would happen next.

Sure enough, he was exactly right.

“Mukyung is hovering between life and death?!”

At Jin Wikyung’s roar, the Lower District Sect member blinked.

“Y-yes?”

“Pung Yang! You dare kill my little brother!”

First Jin Wikyung turned a considerable injury into hovering between life and death, and now he’d pronounced Mukyung dead outright. The Lower District Sect member finally came to his senses and hurriedly opened his mouth.

“Lesser Family Head, I think there’s been a terrible misunderstanding...”

“I’ll tear your limbs to shreds and scatter them across the Nine Provinces!”

“...”

“...”

Jin Wikyung’s anger did not subside until another day had passed.

“Mukyung and Taekyung left the Mount Heng Sword Sect yesterday?”

“Yes. So please take it down a notch.”

“Are they both safe?”

“If they weren’t, would they be coming in a carriage instead of being carried in on a cart?”

“Then...”

“You should be able to see them around noon tomorrow.”

The thought that he could finally rest brought Wipeng immense relief.

*Who am I?*

He was a Peak master, a skilled martial artist known by the epithet Ghost Sword. He had enough ability to claim an important position wherever he went, yet because he had chosen the wrong lord to serve, he was being subjected to this extreme labor.

*When was the last time I had a drink?*

Today, at last, he would be able to enjoy some roast duck with a warm glass of liquor.

A satisfied smile had just appeared around Wipeng’s lips when Jin Wikyung spoke.

“Good. Then let’s get ready.”

“Pardon? Get ready for what?”

“My brothers overcame countless hardships and successfully completed their mission. We have to hold a welcoming ceremony.”

“...Did I spend more than half a month touring the martial world for fun?”

“Hm? Who? Oh, you?”

Jin Wikyung blinked at Wipeng, then let out a hearty laugh.

“Of course that includes you! Surely you didn’t think I’d forgotten?”

*I’d thought surely not, but this guy had definitely forgotten.*

As Wipeng stared at him in disbelief, opening and closing his mouth without a word, Jin Wikyung continued.

“Oh, have your subordinates buy some cloth from a nearby fabric shop. As large as possible.”

“Cloth? Why do we suddenly need that?”

“I have an idea.”

* * *

“...And that’s how it happened.”

Listening to Wipeng, who looked ten years older than when I’d last seen him, I glanced around.

We had reached Sakju two days after leaving the Mount Heng Sword Sect. The city was unexpectedly packed with people, and at the entrance, a gigantic white cloth bearing black writing fluttered in the wind.



Congratulations on the safe return of Jin Mukyung, Jin Taekyung, and Hyuk Mujin!

—Everyone in the Jin Family of Taiyuan—



A groan escaped me before I could stop it.

“Oh, fuck. What the hell is that...?”

In all my life, I had never seen anything like it.

The banner was more than twenty jang—over sixty meters—wide.[^1] Strung between the tops of two pavilions facing each other across a broad avenue, it looked as though it might even be visible from the Mount Heng Sword Sect.

*Look at that unnecessarily flamboyant calligraphy.*

Even overbearing parents whose child had been accepted into a prestigious university wouldn’t go this far.

Jin Mukyung, Hyuk Mujin, and I all stared at the banner with our mouths hanging open, as if we had planned it.

“Why is my name so small?”

I looked again to see what he meant. Hyuk Mujin’s name had been included in tiny letters.

“Are you disappointed that the letters are small? I’d be happy if I were you.”

“It’s strange. You can barely see it from below.”

“Want me to remove my name and put yours there instead? I’m serious.”

Hyuk Mujin thought about it for a moment before answering.

“Now that I think about it, this is fine as it is.”

“Then shut up.”

“Yes, sir.”

The conversation could go no further. The overbearing parent—no, Jin Wikyung—came running toward us with the brightest smile in the world.

“You little rascals!”

Was he a man or a brown bear?

The giant, well over two meters tall, dragged Jin Mukyung and me close with hands as large as pot lids. His brute strength was so tremendous that it would not have been strange if he had crushed us to pieces.

“I’m so glad you’re safe. Really, so glad!”

We had been safe.

Right up until Jin Wikyung hugged us with all his strength.

*Crack.*

“Guh!”

“Mukyung!”

...He doesn’t look very safe now.

The perpetrator, still embracing his victim as he trembled in pain, shouted,

“Doctor! Doctor!”

“I think we should call a doctor. He looks like he’s in real pain.”

Wipeng answered my question with a weary expression.

“Is this your first day dealing with him? I knew this would happen, so I called one in advance.”

“Ohhh.”

It was the first time I had ever thought Wipeng was magnificent.

* * *

The three Jin brothers of the Jin Family of Taiyuan, including me, and Wipeng gathered together shortly after sunset.

When Jin Mukyung appeared wrapped in even thicker bandages, Jin Wikyung cautiously studied him.

“Are you all right?”

“Would you be all right if it were you, my lord? How could you handle someone who was already injured so roughly?”

“I was being as gentle as I could...”

Jin Wikyung might not have been the strongest in martial arts, but when it came to raw physical strength, he was number one in Shanxi.

I quietly slid my chair farther away, while Jin Mukyung answered with a haggard expression.

“I’m fine.”

“...”

He looked anything but fine.

It was fortunate that Jin Mukyung was a Peak master. If he had been an ordinary civilian who had never learned martial arts, he would not have been able to walk.

Wipeng spoke up.

“I heard that the Second Young Master was injured, but I didn’t realize it was this severe. His Internal Injury hasn’t even healed completely yet...”

“Was this really the work of that Pung Yang bastard?”

In response to their questions, Jin Mukyung nodded calmly.

“He was strong. Stronger than I expected.”

Who was Jin Mukyung? He was a promising young prodigy who drew attention throughout the realm. Based on his dazzling talent and relentless effort, he had reached the Peak realm at a young age—yet he had been defeated by a mere mounted-bandit leader.

“You mean he was truly that powerful?”

“Pung Yang... I’ve heard that there are some fairly skilled masters among the mounted bandits of the plateau. But still...”

Their gazes suddenly turned toward me.

It was a silent demand that I stop stuffing my face with roast duck and say something.

I swallowed the food filling my mouth and opened it.

“It’s true. You’ve heard the news about the Great Hero known as the Tiger of Mount Heng, right? He got his arms and legs wrecked too. These days, he gets around in a wheelchair.”

“What is a wheelchair?”

“Ah, a cart. A cart.”

Jin Wikyung tapped the table with one thick finger.

“A master of that caliber would have been known long ago. Mukyung, is it possible that you let your guard down?”

This time, Jin Mukyung shook his head without hesitation.

“I was caught by a move I hadn’t anticipated, but that cannot be an excuse. Even if we fought again, the result would be the same.”

“...Was he really that strong?”

“He used Body-Protecting Qi. It was overwhelming.”

Jin Wikyung and Wipeng both opened their eyes wide.

“Body-Protecting Qi!”

“Second Young Master, is that true?”

There was no need for an answer. Jin Mukyung had no reason to tell such an obvious lie. Facing their shock, he continued.

“He was the strongest opponent I’ve ever fought. No—in exact terms, it would be more accurate to say that he became stronger.”

“Became stronger?”

“What do you mean by that...?”

“The moment he swallowed a crimson pill, he became terrifyingly powerful.”

At last, the conversation had reached the Temporary Strength Pill.

I tried to act as naturally as possible.

*I can’t let them find out I have it.*

The Temporary Strength Pill was a poisoned chalice. It was unquestionably ominous and suspicious, but there was no denying that it possessed tremendous power.

I had already decided to use it as a second-worst contingency for the worst possible moment—when I was facing death.

“It was only for a brief moment, but when he was about to take the pill, I clearly saw that one pill remained inside the wooden case...”

Jin Mukyung let his voice trail off and looked at me.

“Did you happen to find anything on Pung Yang’s person afterward?”

“Something like what?”

“A wooden case. Or the red pill I mentioned.”

I deliberately furrowed my brow.

“I’m not sure. I searched him later to see if he had anything, but all that came spilling out were piles of wooden scraps. Could those have been fragments of the case?”

“Then the pill? The pill?”

“No idea. I was exhausted enough to die myself. How was I supposed to search through everything?”

It was a fairly convincing excuse.

It wasn’t as if only one or two people had died, and the battle had been brutally fierce. It was only natural that I had been too exhausted to search properly. What more could he say?

“Is that so?”

“The people from the Mount Heng Sword Sect might have found it. Or it could have melted into one of the countless pools of blood scattered across the ground.”

“Hmm.”

Jin Mukyung stared at me with faint suspicion, but I merely shrugged.

*You won’t find it even if you search, idiot.*

I had tucked it safely into a corner of the greatest vault in existence—my Inventory, which only I could open and close. Neither Jin Mukyung nor the greatest thief under heaven could touch a hair of the Temporary Strength Pill.

*It really is convenient.*

As I marveled at the convenience of the system once again, Jin Wikyung and Wipeng began speculating about the pill’s origin.

“It must be a relic of demonic, heterodox arts. I remember hearing that quite a few pills with similar effects were used during the Great Faction War.”

“There was a time when the northern part of Shanxi, including Gaoyuan, fell into the hands of the Demonic Cult. If Pung Yang discovered traces of it, that would make sense.”

I had been listening with my ears perked up when I suddenly froze.

*Wait. The Demonic Cult?*

The Demonic Cult was a regular fixture you could never leave out of a Murim novel, the licorice in every medicine shop, and Geum Jandi’s honorary firefighter.[^2]

Of course, it wasn’t a religious organization devoted to world peace and helping the poor. It was more like IS—the Islamic terrorist group.

In short, it was a fanatical organization with absolutely nothing to gain from getting involved with it.

*If the Demonic Cult created the Temporary Strength Pill...*

Pung Yang’s eyes had been stained red, like a demon that had just climbed out of hell. The pill had granted him an absurd amount of power, even if only temporarily.

*I was starting to get the picture.*

It felt bad. Really, really bad!

But nothing could be gained without suffering. The side effects should be something I could endure...

“The most famous thing the Demonic Cult used back then was the Blood-Exploding Pill, if I remember correctly.”

“I’ve only heard of it. They say that once two shichen pass, all the blood vessels in the body burst and the user dies?”

“That was the price of trying to gain power through dark arts.”

“If the Blood-Exploding Pill was that bad, how severe would the side effects of the one Pung Yang used be?”

“I don’t know, but they must be beyond imagination. It wouldn’t just damage his innate qi. Once the time limit ended, his body would suffer tremendous strain. In the end, the pill uses the body itself as kindling and burns it for a brief period.”

I swallowed dryly. Before I knew it, my voice had jumped out.

“What happens after that?”

“It was made by the Demonic Cult. What else would you expect? Once the demonic qi surges into your very marrow… you’d become a murderous fiend who knows nothing but blood.”

“...A murderous fiend? The demonic qi surges into his marrow?”

“If such an object fell into the hands of a villain, it would be a truly terrible disaster... Taekyung, what’s wrong?”

Jin Wikyung looked at me with concern. I rubbed my forehead and found it covered in beads of sweat.

“Nothing. I’m just a little hot.”

“What are you talking about? It’s snowing outside.”

“What would a Soeumin know? I’m a Taeyangin.[^3] That’s why…”

Damn it. I didn’t even know what I was saying anymore.

I gave the other three an awkward smile.

“There’s something I forgot earlier.”

“...?”

“...?”

“...?”

“That pill. Now that I think about it, I have it. Heh-heh. Heh-heh-heh.”

“...!”

“...!”

“...!”

[^1]: A jang is a traditional Korean unit of length measuring roughly three meters.

[^2]: Geum Jandi is the heroine of the Korean drama *Boys Over Flowers*.

[^3]: Soeumin and Taeyangin are two of the four constitutional types in traditional Korean Sasang medicine.
```
